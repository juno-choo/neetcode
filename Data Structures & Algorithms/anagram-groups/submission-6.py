class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            comp = [0]*26

            for c in s:
                idx = ord(c) - ord('a')
                comp[idx] += 1

            anagrams[tuple(comp)].append(s)

        res = []
        for item in anagrams.values():
            res.append(item)
        
        return res


