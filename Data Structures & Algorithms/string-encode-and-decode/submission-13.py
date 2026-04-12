class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedStr = ""

        for string in strs:
            encodedStr += "*"+str(len(string))+"*"+string

        return encodedStr

    def decode(self, s: str) -> List[str]:
        
        decodedStrings = []

        start = end = False

        for i in range(len(s)):
            
            if s[i] == "*" and (not start) and (not end):
                start = True
                lenString = ""
            
            elif start and (not end):
                if s[i] != "*":
                    lenString += s[i]
                else:                    
                    if lenString.isdigit():
                        end = True
                        lenStringAsInt = int(lenString)
                        decodedStrings.append(s[i+1:i+lenStringAsInt+1])
                        start = end = False
                    else:
                        # start = True
                        lenString = ""

        return decodedStrings
