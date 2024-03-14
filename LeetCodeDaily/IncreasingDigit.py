low = 100
high = 300

temp = low
res = []
while(temp > 9):
    temp = temp // 10
first = temp
print("First", first)
current = first
trial = first

while trial < high:
    possible = trial*10 + (current+1)
    if(low < possible < high):
        res.append(possible)
        
    current += 1
    trial = possible
    
    if trial > high:
        trial = first + 1
        current = trial + 1
    print(res)
        
print(res)