# Optimized the scraping process, specially for dhara
# PS: Output is not tested but should be better than previous one

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from sqlalchemy import *
import time

# TODO: Give your database connection code

conn = create_engine("mysql+pymysql://root:srshah@localhost:3306/dharu")
districts = ['Ahemadnagar', 'Akola', 'Amarawati', 'Aurangabad', 'Bandra(E)', 'Beed', 'Bhandara', 'Buldhana', 'Chandrapur', 'Dharashiv(Usmanabad)', 'Dhule', 'Gadchiroli', 'Gondiya', 'Hingoli', 'Jalana', 'Jalgaon',
             'Kolhapur', 'Latur', 'Mumbai', 'Nagpur', 'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Parbhani', 'Pune', 'Raigad', 'Ratnagiri', 'Sangli', 'Satara', 'Sholapur', 'Sindhudurg', 'Thane', 'Vashim', 'Wardha', 'Yavatmal']

state = ['MH', 'Maharashtra']

end_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months_end_date = dict(zip(months, end_date))

for index, district in enumerate(districts):
    index += 1
    district_start = time.time()
    date_counter = 0
    for month in months:
        month_start = time.time()
        for i in range(0, months_end_date[month], 5):
            from_date = i + 1
            # To ensure the end date doesn't exceed the month's last date
            to_date = min(i + 5, months_end_date[month])
            o_url = f"https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=1&Tx_State=MH&Tx_District={index}&Tx_Market=0&DateFrom={from_date}-{month}-2023&DateTo={to_date}-{month}-2023&Fr_Date={from_date}-{month}-2023&To_Date={to_date}-{month}-2023&Tx_Trend=0&Tx_CommodityHead=Wheat&Tx_StateHead=Maharashtra&Tx_DistrictHead={district}&Tx_MarketHead=--Select--"
            # Fetching Data
            response = requests.post(o_url)
            soup = bs(response.content, "html.parser")

            table = soup.find(
                lambda tag: tag.name == "table"
                and tag.has_attr("id")
                and tag["id"] == "cphBody_GridPriceData"
            )
            # rows = table.findAll(lambda tag: tag.name == "tr")
            data = []
            # columns = ['Slno', 'District Name', 'Market Name', 'Commodity', 'Variety', 'Grade', 'Min Price (Rs./Quintal)', 'Max Price (Rs./Quintal)', 'Modal Price (Rs./Quintal)', 'Price Date']
            try:
                for tr in table.find_all("tr"):
                    data.append([td.get_text(strip=True)
                                for td in tr.find_all("td")])
            except:
                print("Error in:", month, ": ", from_date, " - ", to_date)

            # Handelling Empty dataset
            if len(data[1]) < 10:
                continue
            columns = [i.get_text(strip=True) for i in table.find_all("th")]
            res = pd.DataFrame(data, columns=columns)

            # Manipulate Types
            res.drop(columns=['Grade'], inplace=True)
            res["Price Date"] = pd.to_datetime(res['Price Date']).dt.date
            res["Min Price (Rs./Quintal)"] = res["Min Price (Rs./Quintal)"].astype(float)
            res["Max Price (Rs./Quintal)"] = res["Max Price (Rs./Quintal)"].astype(float)
            res["Modal Price (Rs./Quintal)"] = res["Modal Price (Rs./Quintal)"].astype(float)

            # insert into db

            res.to_sql("mh_wheat", conn,
                       if_exists='append', index=False)

        month_end = time.time()
        print(month, 'Done in', month_end - month_start, 'sec')
    date_counter += 1
    district_end = time.time()
    print(district, 'Done in', district_end - district_start, 'sec')
