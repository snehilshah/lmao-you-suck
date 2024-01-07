s = "scayofdzca"

left = 0
right = 1
max_len = -1

while right < len(s) and left < len(s):
    print(left, right, max_len, s[left : right + 1])
    if s[right] == s[left]:
        max_len = max(max_len, right - left - 1)
        left = right
        right += 1
    else:
        right += 1

print(max_len)
