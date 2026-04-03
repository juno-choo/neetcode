class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l, r = 0, 0
        maxLength = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            length = r - l + 1
            maxLength = max(length, maxLength)
            r += 1

        return maxLength

        # "zxyazaya"
        # l
        #      r
