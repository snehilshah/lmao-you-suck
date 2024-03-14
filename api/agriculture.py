import requests
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter
import pandas as pd
from sqlalchemy import *
import time


def get_types(df):
    df["Price Date"] = pd.to_datetime(df["Price Date"])
    df["Price Date"] = df['Price Date'].dt.date
    df["Min Price (Rs./Quintal)"] = df["Min Price (Rs./Quintal)"].astype(float)
    df["Max Price (Rs./Quintal)"] = df["Max Price (Rs./Quintal)"].astype(float)
    df["Modal Price (Rs./Quintal)"] = df["Modal Price (Rs./Quintal)"].astype(float)
    df.drop(columns=['Grade'], inplace=True)
    return df


def db_connect():
    conn = create_engine("mysql+pymysql://root:srshah@localhost:3306/dharu")
    return conn


def insert_db(df):
    df.to_sql("mh_wheat", db_connect(), if_exists='append', index=False)


def fetch_data(url):
    # retry = Retry(connect=10, backoff_factor=0.5)
    response = requests.post(url, HTTPAdapter(max_retries=10))
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


commodity = [[17, "Apple"], [1, "Wheat"]]

districts = ['Ahemadnagar', 'Akola', 'Amarawati', 'Aurangabad', 'Bandra(E)', 'Beed', 'Bhandara', 'Buldhana', 'Chandrapur', 'Dharashiv(Usmanabad)', 'Dhule', 'Gadchiroli', 'Gondiya', 'Hingoli', 'Jalana', 'Jalgaon',
             'Kolhapur', 'Latur', 'Mumbai', 'Nagpur', 'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Parbhani', 'Pune', 'Raigad', 'Ratnagiri', 'Sangli', 'Satara', 'Sholapur', 'Sindhudurg', 'Thane', 'Vashim', 'Wardha', 'Yavatmal']



state = ['MH', 'Maharashtra']

days = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25], [26, 30]]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for index, district in enumerate(districts):
    index += 1
    district_start = time.time()
    for month in months:
        month_start = time.time()
        for date in days:
            from_date = date[0]
            to_date = date[1]
            if to_date == 30 and month == 'Feb':
                to_date = 28
            o_url = f"https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=1&Tx_State=MH&Tx_District={index}&Tx_Market=0&DateFrom={from_date}-{month}-2023&DateTo={to_date}-{month}-2023&Fr_Date={from_date}-{month}-2023&To_Date={to_date}-{month}-2023&Tx_Trend=0&Tx_CommodityHead=Wheat&Tx_StateHead=Maharashtra&Tx_DistrictHead={district}&Tx_MarketHead=--Select--"
            res = fetch_data(o_url)
            if res.empty:
                continue
            typed = get_types(res)
            insert_db(typed)
        month_end = time.time()
        print(month, 'Done in', month_end - month_start, 'sec')
    district_end = time.time()
    print(district, 'Done in', district_end - district_start, 'sec')
