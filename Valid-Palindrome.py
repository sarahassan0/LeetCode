class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1 
        while l <= r:

            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
        
# -------------- O(n) time, O(n) space -----------------

        # text = [] # more effiecinat than string , because pyhton creats new string in every appeand which leads to O(n2)

        # for c in s:
        #     if c.isalnum():
        #         text.append(c.lower())
        # return text == text[::-1]


            