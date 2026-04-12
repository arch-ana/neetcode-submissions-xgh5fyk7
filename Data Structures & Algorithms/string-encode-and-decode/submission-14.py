class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedStr = ""

        for string in strs:
            encodedStr += "*"+str(len(string))+"*"+string

        return encodedStr

    def decode(self, s: str) -> List[str]:
        
        decodedStrings = []

        start = False

        for i in range(len(s)):
            
            if s[i] == "*" and (not start):
                start = True
                lenString = ""
            
            elif start:
                if s[i] != "*":
                    lenString += s[i]
                else:                    
                    if lenString.isdigit():
                        lenStringAsInt = int(lenString)
                        decodedStrings.append(s[i+1:i+lenStringAsInt+1])
                        start = False
                    else:
                        lenString = ""

        return decodedStrings
