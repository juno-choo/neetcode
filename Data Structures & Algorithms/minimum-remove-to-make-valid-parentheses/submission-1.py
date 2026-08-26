class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # use stack to find valid parantheses
        st = []
        openB = 0

        for c in s:
            if openB == 0 and c == ')': continue
            if c == ')':
                st.append(c)
                openB -= 1

            elif c == '(':
                openB += 1
                st.append(c)

            else:
                st.append(c)

        ptr = len(st) - 1

        res = []
        while ptr >= 0:
            if openB > 0 and st[ptr] == '(':
                openB -= 1
            else:
                res.append(st[ptr])
            ptr -= 1
        return "".join(res[::-1])
            

        # keep count of open brackets, if not even at the end, ignore

        # if zero open brackets and we encounter ')', ignore