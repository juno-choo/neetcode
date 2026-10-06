class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # bottom up tabulation
        # time: O(n*m*k), space: O(n)
        n = len(s)
        dp = [False] * (n + 1)

        # The empty suffix can always be segmented
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                length = len(word)

                if s[i:i + length] == word and dp[i + length]:
                    dp[i] = True
                    break

        return dp[0]