class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for n in digits:
            s+= str(n)

        s = str(int(s) + 1)
        return [int(i) for i in s]
        
        