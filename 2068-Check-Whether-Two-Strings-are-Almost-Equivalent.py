class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        freq = {}

        for i in range(len(word1)):
            if word1[i] in freq:
                freq[word1[i]] = freq[word1[i]] + 1
            else: freq[word1[i]] = 1

            if word2[i] in freq:
                freq[word2[i]] = freq[word2[i]] - 1
            else: freq[word2[i]] = -1


        return max(freq.values()) <=3 and min(freq.values()) >= -3
        