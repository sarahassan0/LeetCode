class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 1

        while i < len(arr):
            if arr[i-1] == 0:
                arr[i+1:] = arr[i: len(arr) - 1]
                arr[i] = 0
                i += 1
            i += 1
