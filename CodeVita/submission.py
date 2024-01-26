def consistPalindrome(s):
    s = s.lower()
    for i in range(len(s) - 1):
        if s == s[::-1]:
            return True
        else:
            s = s[1:]

def eliminate_round1(round1_names):
    initials = ""
    for i, name in enumerate(round1_names):
        initials += str(name[0])

        if consistPalindrome(initials):
            round1_names.pop(i)
            initials = initials[:-1]
    return round1_names


def eliminate_round2(names, n):
    while len(names) > 1:
        names.pop(n - 1)
    return names[0]


input_names = input().split()
n = int(input().strip())
round1_winner = eliminate_round1(input_names)
print(round1_winner)
winner = eliminate_round2(round1_winner, n)
print(winner, end="")
