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

            # print("Current i: ")
            # print(i)
            
            if s[i] == "*" and (not start) and (not end):
                start = True
                lenString = ""
            
            elif start and (not end):
                if s[i] != "*":
                    # print("s[i] is: "+s[i]+"\n")
                    lenString += s[i]
                else:                    
                    if lenString.isdigit():
                        end = True
                        # print("lenString is: "+lenString+"\n")
                        lenStringAsInt = int(lenString)
                        # print("word is: "+s[i+1:i+lenStringAsInt+1]+"\n")
                        decodedStrings.append(s[i+1:i+lenStringAsInt+1])
                        start = end = False
                    else:
                        # print("Not digit\n")
                        # print("s[i] is: "+s[i]+"\n")
                        start = True
                        lenString = ""

        return decodedStrings
