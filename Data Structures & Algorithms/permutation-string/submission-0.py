class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        needed = {}
        for c in s1:
            needed[c] = needed.get(c, 0) + 1
        window = {}
        for c in range(0, len(s1)):
            window[s2[c]] = window.get(s2[c], 0) + 1
        
        l, r = 0, len(s1) - 1

        while r < len(s2):
            if needed == window:
                return True
            
            window[s2[l]] -= 1
            if window[s2[l]] == 0: del window[s2[l]]
            l += 1

            r += 1
            if r >= len(s2): return False
            window[s2[r]] = window.get(s2[r], 0) + 1
            
        return False