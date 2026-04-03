class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for i in range(len(s)):
            sMap[s[i]] += 1

        for i in range(len(t)):
            tMap[t[i]] += 1

        return sMap.items() == tMap.items()
        


