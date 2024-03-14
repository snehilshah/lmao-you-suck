import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

commodity = {"Ajwain": 137, "Alasande Gram": 281}
state = []

response = requests.post(
    f"https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=1&Tx_State=MH&Tx_District=1&Tx_Market=0&DateFrom=26-Jan-2023&DateTo=30-Jan-2023&Fr_Date=26-Jan-2023&To_Date=30-Jan-2023&Tx_Trend=0&Tx_CommodityHead=Wheat&Tx_StateHead=Maharashtra&Tx_DistrictHead=Ahmednagar&Tx_MarketHead=--Select--",
)
soup = bs(response.content, "html.parser")

table = soup.find(
    lambda tag: tag.name == "table"
    and tag.has_attr("id")
    and tag["id"] == "cphBody_GridPriceData"
)
columns = [i.get_text(strip=True) for i in table.find_all("th")]
# rows = table.findAll(lambda tag: tag.name == "tr")
data = []
# columns = ['Slno', 'District Name', 'Market Name', 'Commodity', 'Variety', 'Grade', 'Min Price (Rs./Quintal)', 'Max Price (Rs./Quintal)', 'Modal Price (Rs./Quintal)', 'Price Date']
for tr in table.find_all("tr"):
    data.append([td.get_text(strip=True) for td in tr.find_all("td")])

# res = pd.DataFrame(data)

df = pd.DataFrame(data, columns=columns)
print(len(df.columns))
print(df.head())
df["Price Date"] = pd.to_datetime(df["Price Date"])

