class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # if len(arr) == 1:
        #     return [-1]
        max_num = -1

        for i in range(len(arr) - 1, -1, -1):
    
            arr[i], tmp = max_num, arr[i]
            max_num = max(tmp, max_num)

        return arr