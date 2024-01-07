from collections import Counter

nums = [19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]

res = -1

frequency = Counter(nums)
print(frequency)

for value in frequency.values():
    if value == 1:
        print(False)
        break
    res += value // 3 + 1

print(res + 1)