class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s) -1

        for i in range(length//2+1):
            s[i], s[length - i]  = s[length - i], s[i]