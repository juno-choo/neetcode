class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            else:
                s_dict[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in t_dict:
                t_dict[t[j]] = 0
            else:
                t_dict[t[j]] += 1

        return t_dict == s_dict
