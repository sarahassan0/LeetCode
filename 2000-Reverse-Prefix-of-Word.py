class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word:
            return word
        
        ch_index = word.index(ch)
        prefix = word[:ch_index + 1] 

        
        return "".join([prefix[::-1] + word[ch_index + 1:]])
        