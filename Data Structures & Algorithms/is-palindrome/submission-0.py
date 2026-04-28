class Solution:
    def isPalindrome(self, s: str) -> bool:

        start, end = 0, len(s) - 1

        while end >= start:
            if s[start] == " " or not s[start].isalnum():
                start += 1
            elif s[end] == " " or not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
                # continue

        return True

            
        