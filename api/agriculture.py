import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

response = requests.post(
    "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=17&Tx_State=DL&Tx_District=1&Tx_Market=4747&DateFrom=01-Jan-2023&DateTo=24-Jan-2024&Fr_Date=01-Jan-2023&To_Date=24-Jan-2024&Tx_Trend=2&Tx_CommodityHead=Apple&Tx_StateHead=NCT+of+Delhi&Tx_DistrictHead=Delhi&Tx_MarketHead=Azadpur",
)

soup = bs(response.content, "html.parser")

table = soup.find(
    lambda tag: tag.name == "table"
    and tag.has_attr("id")
    and tag["id"] == "cphBody_GridViewBoth"
)
rows = table.findAll(lambda tag: tag.name == "tr")


output = open("output.txt", "wb")
for row in rows:
    output.write(str(row.text).encode("utf-8"))


output.close()
