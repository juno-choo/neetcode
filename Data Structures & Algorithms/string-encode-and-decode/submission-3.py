class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            num = len(s)
            encoded += str(num) + '@' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            word = ''
            delim = ''

            while s[i] != '@':
                delim += s[i]
                i += 1
            i += 1
            j = 0
            while j < int(delim):
                word += s[j + i]
                j += 1
            res.append(word)
            i += int(delim)
        return res