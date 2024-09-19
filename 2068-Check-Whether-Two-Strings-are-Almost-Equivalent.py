class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        freq = {}
        # for i in range(n):
        #     if word1[i] in freq1:
        #         freq1[word1[i]] = freq1[word1[i]] + 1
        #     else: freq1[word1[i]] = 0


        #     if word2[i] in freq2:
        #         freq2[word2[i]] = freq2[word2[i]] + 1
        #     else: freq2[word2[i]] = 0

        # for k, v in freq1.items:
        #     if k in freq2[k]:
        #         if v - freq2[k]

        for i in range(len(word1)):
            if word1[i] in freq:
                freq[word1[i]] = freq[word1[i]] + 1
            else: freq[word1[i]] = 1
        print(freq)

        for i in range(len(word1)):

            if word2[i] in freq:
                freq[word2[i]] = freq[word2[i]] - 1
            else: freq[word2[i]] = -1

        print(freq)
        return max(freq.values()) <=3 and min(freq.values()) >= -3
        