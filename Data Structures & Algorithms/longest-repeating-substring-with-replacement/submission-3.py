class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        maxF = 0
        l = 0
        res = 0

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            maxF = max(maxF, charMap[s[r]])
            
            while (r - l + 1) - maxF > k and l < r:
                charMap[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res

             


        