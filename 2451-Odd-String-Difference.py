class Solution:
    def oddString(self, words: List[str]) -> str:
        
        hashMap = {}


        for w in words:
            difference = []
            print(hashMap, "out loop")
            for i in range(1, len(w)):
                difference.append((ord(w[i]) - 97) - (ord(w[i-1]) - 97) )

            difference = str(difference)

            if difference in hashMap:
                hashMap.pop(difference)
            else:
                hashMap[difference] = w

        return  list(hashMap.values())[0]
