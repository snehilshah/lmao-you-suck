def longestPalindrome(s):
    for i in range(len(s) - 1):
        if s == s[::-1]:
            return True
        else:
            s = s[1:]


def eliminate_round1(round1_names):
    initials = ""
    for i, name in enumerate(round1_names):
        initials += str(name[0])

        if longestPalindrome(initials):
            round1_names.pop(i)
            initials = initials[:-1]
    return round1_names


def round2(names, n):
    while len(names) > 1:
        names.pop(n - 1)
    return names[0]


names_input = input().strip().split()
print(names_input)
n = int(input().strip())
winner = eliminate_round1(names_input)

res = round2(winner, n)
print(winner)
