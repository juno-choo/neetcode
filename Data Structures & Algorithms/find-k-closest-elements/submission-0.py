class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        # if x <= arr[0], we take arr[:k]
        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[n-k:]

        # Algo 2: binary search
        # if x <= arr[m], search left

        # if arr[m] < x, search right 
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            if x <= arr[m]:
                r = m
            else:
                l = m + 1

        r = l
        l = r - 1
# # [1,2,3,4,5], k = 4, x = 3
#          r
#    l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r == n:
                l -= 1

            elif abs(x - arr[l]) <= abs(x - arr[r]):
                l -= 1
            else:
                r += 1

        return arr[l+1:r]