class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for char in s:
            if char != ']':
                st.append(char)

            else:
                cur = ""
                while st and st[-1] != '[':
                    cur = st.pop() + cur
                st.pop()

                num = ""
                while st and st[-1].isdigit():
                    num = st.pop() + num

                st.append(int(num) * cur)

        return ''.join(st)
                