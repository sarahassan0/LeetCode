class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0

        valid = 0
        for i in range(len(flowerbed)-1):
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                valid += 1
                continue
            if flowerbed[i]==0:
                if flowerbed[i+1] == 0 :
                    if flowerbed[i-1]== 0:
                        flowerbed[i] = 1
                
                        valid += 1 
                    elif i+1 == len(flowerbed) - 1 :
                        flowerbed[i+1] = 1
                        valid += 1
        print(flowerbed)
        return valid >= n