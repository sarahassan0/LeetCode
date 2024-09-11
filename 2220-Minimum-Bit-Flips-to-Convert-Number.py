class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(format(start, '08b'))
        goal = str(format(goal, '08b'))
        longest = start if len(start) > len(goal) else goal
        short = start if longest != start else goal
        
        leng = max(len(start), len(goal)) - len(short)
        short = '0' * leng + short
        
        flip = 0
        for i in range(len(short)):
            if longest[i] != short[i]:
                flip += 1
           
        return flip 
