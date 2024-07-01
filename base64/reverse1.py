import pyodbc
import time
import base64
import binascii


query1 = "SELECT MNoFinal, Mper, MPhotoURL from JJCMembers2024_25 where convert(int,MNoFinal)<3045 ORDER BY MNoFinal, Mper;"

queries = [
    query1,
]


# query2 = "SELECT MNoFinal, Mper, MPhotoURL from JJCMembers2024_25 where convert(int,MNoFinal)>=3084 and convert(int,MNoFinal)<3085 ORDER BY MNoFinal, Mper;"

# query3 = "SELECT MNoFinal, Mper, MPhotoURL from JJCMembers2024_25 where convert(int,MNoFinal)>=4000 and convert(int,MNoFinal)<5000 ORDER BY MNoFinal, Mper;"
# query4 = "SELECT MNoFinal, Mper, MPhotoURL from JJCMembers2024_25 where convert(int,MNoFinal)>=5000 and convert(int,MNoFinal)<6000 ORDER BY MNoFinal, Mper;"
# query5 = "SELECT MNoFinal, Mper, MPhotoURL from JJCMembers2024_25 where convert(int,MNoFinal)>=6000 and convert(int,MNoFinal)<7000 ORDER BY MNoFinal, Mper;"
# query6 = "SELECT MNoFinal, Mper, MPhotoURL from JJCMembers2024_25 where convert(int,MNoFinal)>=7000 ORDER BY MNoFinal, Mper;"

# MNOFinal_MPer.jpg
RED = '\033[31m'
RESET = '\033[0m'


def base_64_to_image(base64_string, mno, mper):
    try:
        image = base64.b64decode(base64_string, validate=True)
        file_to_save = f"D:/Papa/FinalImg/Iter1/{mno}_{mper}.jpg"
        with open(file_to_save, "wb") as f:
            f.write(image)
    except binascii.Error as e:
        print(e)


def db_connection():
    server = '199.231.93.236'
    database = '02jjcnavimumbai_com'
    username = 'usrDBJJCNaviMumbai'
    password = 'rahe_10O10'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password,)
    return cnxn


for query in queries:
    start = time.time()
    cursor = db_connection().cursor()
    cursor.execute(query)

    counter = 0
    fetched_rows = cursor.fetchall()
    for row in fetched_rows:
        try:
            mno = row[0]
            mper = row[1]
            mphoto = row[2]
            mphoto = mphoto.split(",")[1]
        except Exception as e:
            print(e)
            print(f"{RED}Error in fetching data from database at{RESET}")
            print(mno, mper, mphoto)
        print(f"Starting for {mno}_{mper}")
        # start = time.time()

        base_64_to_image(mphoto, mno, mper)
        counter += 1

    end = time.time()
    print(f"Time taken to fetch data: {end-start} seconds")
