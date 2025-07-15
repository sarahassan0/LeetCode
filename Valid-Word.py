class Solution:
    def isValid(self, word: str) -> bool:
        res = 0
        
        if len(word) < 3:
            res -= 1
        elif not word.isalnum():
            res -= 1
        elif not (set(word.lower()) & set('aeiou')):
            res -= 1
        elif not (set(word.lower()) & set('bcdfghjklmnpqrstvwxyz')):
            res -= 1 
    
        return res == 0
        
        
              
        

        