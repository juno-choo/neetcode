class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])

                if maxL - height[l] > 0:
                    res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])

                if maxR - height[r] > 0:
                    res += maxR - height[r]

        return res
