s = "A man, a plan, a canal: Panama"


left = 0
right = len(s) - 1

while left <= right:
    if s[left].isalnum() == False:
        left += 1
        continue
    if s[right].isalnum() == False:
        right -= 1
        continue
    if s[left].lower() == s[right].lower():
        left += 1
        right -= 1
    else:
        print("False")
        break
print("True")
