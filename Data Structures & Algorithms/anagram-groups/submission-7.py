class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            charFreq = [0] * 26

            for c in s:
                charFreq[ord(c) - ord('a')] += 1

            anagrams[tuple(charFreq)].append(s)

        return list(anagrams.values())