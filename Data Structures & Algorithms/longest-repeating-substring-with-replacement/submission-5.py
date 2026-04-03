class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        length = 0
        maxF = 0

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            maxF = max(maxF, charMap[s[r]])

            while (r - l + 1) - maxF > k:
                charMap[s[l]] -= 1
                l += 1

            length = max(length, (r - l + 1))

        return length