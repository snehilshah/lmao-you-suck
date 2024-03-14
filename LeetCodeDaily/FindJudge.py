from typing import List
from collections import defaultdict


def findJudge(n: int, trust: List[List[int]]) -> int:
    if n == 1:
        return 1
    frequency = defaultdict(int)
    for trustee, trusted in trust:
        frequency[trusted] += 1
        frequency[trustee] -= 1

    for person, freq in frequency.items():
        if freq == n - 1:
            return person
    return -1


# Example usage
n = 3
trust = [[1, 3], [2, 3], [3, 1]]
result = findJudge(n, trust)
print(result)
