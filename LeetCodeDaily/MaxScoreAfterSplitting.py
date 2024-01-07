class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        res = 0
        for c in s:
            if c == "0":
                zero += 1
            else:
                one -= 1
                zero += 1
            res = max(res, zero + one)
        return res


