def isPrefixAndSuffix(str1, str2):
    prefix, suffix = False, False
    if str1 == str2[0:len(str1)]: prefix = True
    if str1 in str2[-len(str1):]: suffix = True    

    return prefix and suffix
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for word in words[i+1:n]:
                if isPrefixAndSuffix(words[i], word):
                    count += 1

        return count
                    





        