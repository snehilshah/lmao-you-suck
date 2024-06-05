from faker import Faker
import pandas as pd
from random import randrange
fake = Faker()

print(randrange(1,4))

memno = []
names = []
for i in range(1001, 1011):
    random_no = randrange(1, 4)
    for j in range(1, random_no+1):
        memno.append(f'{i}_{j}')
        names.append(fake.name())


df = pd.DataFrame({"MemNO": memno, "Mem_Name": names})
df.to_csv("PDF/demo.csv", index=False)
