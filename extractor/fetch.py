from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


response = requests.get("http://127.0.0.1:5500/index.html")

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
table_rows = table.find_all("tr")

data = []
for row in table.find_all("tr"):
    row_data = []
    for cell in row.find_all("td"):
        row_data.append(cell.text)
    data.append(row_data)

df = pd.DataFrame(data)

json_str = df.to_json(orient="records")
json_obj = json.loads(json_str)


with open("./extractor/data.json", "w", encoding="utf-8") as f:
    json.dump(json_obj, f, ensure_ascii=False, indent=4)
    
    
# "Rosewater":"	#f5e0dc"
# "Flamingo":"	#f2cdcd"
# "Pink":"	#f5c2e7"
# "Mauve":"	#cba6f7"
# "Red":"	#f38ba8"
# "Maroon":"	#eba0ac"
# "Peach":"	#fab387"
# "Yellow":"	#f9e2af"
# "Green":"	#a6e3a1"
# "Teal":"	#94e2d5"
# "Sky":"	#89dceb"
# "Sapphire":"	#74c7ec"
# "Blue":"	#89b4fa"
# "Lavender":"	#b4befe"
# "Text":"	#cdd6f4"
# "Subtext1":"	#bac2de"
# "Subtext0":"	#a6adc8"
# "Overlay2":"	#9399b2"
# "Overlay1":"	#7f849c"
# "Overlay0":"	#6c7086"
# "Surface2":"	#585b70"
# "Surface1":"	#45475a"
# "Surface0":"	#313244"
# "Base":"	#1e1e2e"
# "Mantle":"	#181825"
# "Crust":"	#11111b"
