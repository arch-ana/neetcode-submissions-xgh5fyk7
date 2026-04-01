class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for char in s:
            d1[char] += 1
        for char in t:
            d2[char] += 1
        
        return d1 == d2
        