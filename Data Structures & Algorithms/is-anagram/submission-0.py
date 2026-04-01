class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_i = {}
        dict_j = {}

        if len(s) != len(t):
            return False
        else:
            for x in s:
                if x in dict_i:
                    dict_i[x] += 1
                else:
                    dict_i[x] = 1
            for y in t:
                if y in dict_j:
                    dict_j[y] += 1
                else:
                    dict_j[y] = 1
        
        return dict_i == dict_j

        