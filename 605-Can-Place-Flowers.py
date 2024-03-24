class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n <= 1

        valid = 0
        for i in range(len(flowerbed)-1):
  
            if flowerbed[i] == flowerbed[i+1] == 0:

                if i == 0:
                    flowerbed[0] = 1
                    valid += 1
                    continue
                    
                elif flowerbed[i-1]== 0 :
                    flowerbed[i] = 1
                    valid += 1 

                elif i+1 == len(flowerbed) - 1 :
                    flowerbed[i+1] = 1
                    valid += 1

        return valid >= n