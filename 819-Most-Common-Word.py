class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        wordsDict = Counter(re.split(r"[ .,!?;'\s]", paragraph.lower()))
        maxi = (0,0)

        for k, v in wordsDict.items():
            if k and k not in banned and v > maxi[1]:
                maxi = (k, v)


        return maxi[0]