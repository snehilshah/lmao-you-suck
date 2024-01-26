def longestPalindrome(s):
    res = ""
    resLen = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res


# res = longestPalindrome("klj")
# print(res)


def longestPalindrome(s):
    # Find if the last character is causing a palindrome

    for i in range(len(s) - 1):
        if s == s[::-1]:
            return True
        else:
            s = s[1:]


print(longestPalindrome("gfs"))


a = [1, 2, 3, 4]
a.pop()



a = "Snehil"
a = a[:-1]
print(a)


