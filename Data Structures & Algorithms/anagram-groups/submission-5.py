class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1

            freq = tuple(freq)

            if freq in anaMap:
                anaMap[freq].append(s)
            else:
                anaMap[freq] = [s]

        return list(anaMap.values())