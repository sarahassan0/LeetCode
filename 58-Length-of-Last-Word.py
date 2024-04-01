class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        print(arr)
        
        for i in arr:
            if i != "":
                word = i

        return len(word)
        