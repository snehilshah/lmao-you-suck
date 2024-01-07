bank = ["000", "111", "000"]

m = prev = 0
res = 0
for row in bank:
    for c in row:
        if c == "1":
            m += 1
    if m == 0:
        continue
    
    res = res + m * prev
    prev = m
    m = 0
    print(res)
