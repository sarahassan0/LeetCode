class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common_count = Counter(words[0])
        result = []

        for w in words:
            common_count &= Counter(w)    

        for char, count in common_count.items():
            result.extend([char] * count) 
            
        return result
        