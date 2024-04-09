import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from sqlalchemy import *
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Do not bother this
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m' # orange on some systems
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHT_GRAY = '\third-party033[47m'
BACKGROUND_DARK_GRAY = '\033[100m'
BACKGROUND_BRIGHT_RED = '\033[101m'
BACKGROUND_BRIGHT_GREEN = '\033[102m'
BACKGROUND_BRIGHT_YELLOW = '\033[103m'
BACKGROUND_BRIGHT_BLUE = '\033[104m'
BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
BACKGROUND_BRIGHT_CYAN = '\033[106m'
BACKGROUND_WHITE = '\033[107m'
UNDERLINE = '\033[4m'


RESET = '\033[0m' # called to return to standard terminal text color

overall_start = time.time()


state_code = 'MH'
state = 'Maharashtra'
commodity_code = '14'
commodity = 'Sunflower'
# Put the actual year you want to scrape till
start_year = 2013
end_year = 2013        # +1 is done in the loop
table_name = f"{state_code.lower()}_{commodity.lower()}"


month_start = 'Jan'
month_end = 'Dec'
start_date = '1'
end_date = '31'

# If you want to overwrite the table, uncomment the below line
# table_name = 'sjkaldfhskjlh'


def get_types(df):
    df["Price Date"] = pd.to_datetime(
        df['Price Date'], format='mixed').dt.date
    df["Min Price (Rs./Quintal)"] = df["Min Price (Rs./Quintal)"].astype(float)
    df["Max Price (Rs./Quintal)"] = df["Max Price (Rs./Quintal)"].astype(float)
    df["Modal Price (Rs./Quintal)"] = df["Modal Price (Rs./Quintal)"].astype(float)
    df.drop(columns=['Grade'], inplace=True)
    return df


def db_connect():
    conn = create_engine(
        "mysql+pymysql://root:srshah@localhost:3306/web_scrape")
    return conn


def insert_db(df):
    df.to_sql(table_name, db_connect(), if_exists='append', index=False)


def fetch_data(url):
    response = requests.post(url, verify=False)
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

    # print(len(data[1]))
    if len(data[1]) < 10:
        return pd.DataFrame()
    res = pd.DataFrame(data, columns=columns)

    return res


for year in range(start_year, end_year + 1):
    print(f'Starting year {year}....')
    year_start = time.time()
    o_url = f"https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity={commodity_code}&Tx_State={state_code}&Tx_District=0&Tx_Market=0&DateFrom={start_date}-{month_start}-{year}&DateTo={end_date}-{month_end}-{year}&Fr_Date={start_date}-{month_start}-{year}&To_Date={end_date}-{month_end}-{year}&Tx_Trend=0&Tx_CommodityHead={commodity}&Tx_StateHead={state}&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--"
    res = fetch_data(o_url)
    if res.empty:
        print(f"{RED}No data for year {year}{RESET}")
        continue
    typed = get_types(res)
    insert_db(typed)
    year_end = time.time()
    print(f"{GREEN}Year {UNDERLINE}{MAGENTA}{year}{RESET}{GREEN} took {RESET}{UNDERLINE}{YELLOW}{year_end - year_start}{RESET}{GREEN} seconds{RESET}")

overall_end = time.time()
print(f"Overall it took {UNDERLINE}{BLACK}{BACKGROUND_GREEN}{overall_end - overall_start}{RESET} seconds to scrape data for {BLACK}{BACKGROUND_CYAN}{commodity}{RESET} in {BACKGROUND_YELLOW}{BLACK}{state}{RESET} from {UNDERLINE}{BACKGROUND_WHITE}{BLACK}{start_year} - {end_year}{RESET}")
