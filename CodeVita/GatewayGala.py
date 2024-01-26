def check_palindrome(s):
    return s == s[::-1]


def play_rounds(players, n):
    while True:
        palindrome_indices = [i for i, name in enumerate(players) if check_palindrome(name)]
        if not palindrome_indices:
            break
        players.pop(palindrome_indices[0])
    while len(players) > 1:
        players.pop(n - 1)
    return players[0]


names_input = input().strip().split()
n = int(input().strip())
winner = play_rounds(names_input, n)
print(winner)
