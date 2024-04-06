class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        valid = ""
        closed = 0

        for c in s:
            if c == ')':
                if count > 0:
                    valid += c
                    count -= 1
    
            else:
                if c == '(':
                    count += 1
                valid += c

        count = 0
        for i in range(len(valid )- 1, -1, -1):
            if valid[i] == '(':
                if count > 0:
                    count -= 1
                else:
                    valid = valid[0:i] + valid[i+1:]

    
            elif valid[i] == ')':
                count += 1
        return valid