from typing import List
from collections import Counter

def commonChars(self, words: List[str]) -> List[str]:
    res = Counter(words[0])
    for word in words[1:]:
        res &= Counter(word)
    return list(res.elements())