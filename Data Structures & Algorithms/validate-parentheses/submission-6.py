class Solution:
    def isValid(self, s: str) -> bool:
        testList = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                testList.append(char)
            elif char == ")":
                if len(testList)>0 and testList[-1] == "(":
                    testList.pop()
                else:
                    return False
            elif char == "}":
                if len(testList)>0 and testList[-1] == "{":
                    testList.pop()
                else:
                    return False
            elif char == "]":
                if len(testList)>0 and testList[-1] == "[":
                    testList.pop()
                else:
                    return False
            
        return len(testList) == 0