class Solution:

    def encode(self, strs: List[str]) -> str:

        compString = ""

        for string in strs:
            compString = compString + "#" + str(len(string)) + "#" + string

        return compString 


    def decode(self, s: str) -> List[str]:

        strs = []
        delimiters = []
        i = 0

        while i < len(s):
            if s[i] == "#":
                if len(delimiters) <= 1:
                    delimiters.append(i)
                    if len(delimiters) == 2:
                        print(delimiters)
                        length = int(s[delimiters[0]+1:delimiters[1]])
                        i+=length
                        strs.append(s[delimiters[1]+1:delimiters[1]+1+length])
                        delimiters = []
            i+=1
        
        return strs