class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        tMap = Counter(t)
        
        # Initialize variables to keep track of total and formed
        total, formed = len(tMap), 0
        res, idx = float('inf'), (0, 0)
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in tMap:
                tMap[c] -= 1
                if tMap[c] == 0:
                    formed += 1
            
            # Our window is valid
            while formed == total:
                # Update if found a smaller valid window
                if (r - l + 1) < res:
                    res = r - l + 1
                    idx = (l, r)
                # Try and shrink to find smaller valid window
                if s[l] in tMap:
                    if tMap[s[l]] == 0:
                        formed -= 1
                    tMap[s[l]] += 1
                l += 1

        return s[idx[0]:idx[1]+1] if res != float('inf') else ""
                