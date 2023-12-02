sum = 0
l, r = 0, 0
lower = 0
upper = 0
count = 0
with open('./AdventOfCode/Day1/input.txt') as file:
    for line in file:
        lower = 0
        upper = 0
        l = 0
        end = len(line) - 1
        r = end
        while True:
            if line[l].isdigit():
                lower = int(line[l])
                while (r >= 0):
                    if line[r].isdigit():
                        upper = int(line[r])
                        break
                    r -= 1
                break

            if line[r].isdigit():
                upper = int(line[r])
                while (l < end):
                    if line[l].isdigit():
                        lower = int(line[l])
                        break
                    l += 1
                break
            l += 1
            r -= 1
        count += 1
        sum += (lower*10 + upper)
        
print(sum)
