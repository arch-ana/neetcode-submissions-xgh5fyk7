class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        
        for str in strs:
            charArray = [0]*26
            for char in str:
                charArray[ord(char)-ord("a")] += 1
            
            d[tuple(charArray)].append(str)


        return list(d.values())

        