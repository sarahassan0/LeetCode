class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) ==1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0
            return True if flowerbed[0] - n <= 1 or flowerbed[0] - n == -1 else  False

        valid = 0
        for i in range(len(flowerbed)-1):
            # dd = sum(flowerbed[i-1:i+2])
            # print(flowerbed[i-1:i+2])
            # if dd < 2:


            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                valid += 1
                continue
            if flowerbed[i]==flowerbed[i+1] == 0 :
                if flowerbed[i-1]== 0:
                    flowerbed[i] = 1
                # else:
                #     # print(flowerbed[i],flowerbed[i+1] )
                #     flowerbed[i] = 1
                
                    valid += 1 
                if i+1 == len(flowerbed) - 1 and flowerbed[i] ==0:
                    # pass

                    flowerbed[i+1] = 1
                    valid += 1
        print(flowerbed)
        # print(valid)
        return valid >= n