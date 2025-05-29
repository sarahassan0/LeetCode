class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set('aeiou')
        prefix_sum = [0] * (n + 1)
        result = []

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1]
            if words[i-1][0] in vowels and words[i-1][-1] in vowels:
                prefix_sum[i] += 1


        for l, r in queries:
            count = prefix_sum[r+1] - prefix_sum[l]
            result.append(count)

        return result

        