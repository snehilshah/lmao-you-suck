damage = input().strip().split()
size = input().strip().split()
category = input().strip().split()
barracks = int(input().strip())
merged = []
# damage = [8, 9, 4, 9, 1, 8, 1, 5, 6, 8]
# size = [2, 5, 7, 2, 3, 4, 5, 9, 3, 8]
# category = [4, 2, 2, 3, 4, 3, 2, 1, 2, 1]
# barracks = 10
filled = 0
total_dps = 0

for dps, capacity, type in zip(damage, size, category):
    divider = dps / capacity
    merged.append((dps, capacity, type, divider))

merged.sort(key=lambda x: x[3], reverse=True)
print(merged)


istrained = set()

for value in merged:
    if filled == barracks:
        break
    if value[2] in istrained:
        continue
    else:
        if value[1] + filled <= barracks:
            print("selected", (value))
            total_dps += value[0]
            istrained.add(value[2])

print(total_dps)