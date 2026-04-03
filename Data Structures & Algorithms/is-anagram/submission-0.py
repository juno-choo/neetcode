class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)
        for i in t:
            if i not in s_counts:
                return False
            
            s_counts[i] -= 1
            if s_counts[i] == 0:
                del s_counts[i]
        return len(s_counts) == 0