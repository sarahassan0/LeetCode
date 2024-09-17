class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      
        s1 = s1.split()
        s2 = s2.split()

        word_count = Counter(s1 + s2)

        uncommon_words = [w for w, c in word_count.items() if c == 1]

        return uncommon_words
