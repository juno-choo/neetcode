class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        res = 0

        for token in tokens:
            if token == '+':
                a = int(st.pop())
                b = int(st.pop())
                st.append(a + b)

            elif token == '-':
                a = int(st.pop())
                b = int(st.pop())
                st.append(b - a)

            elif token == '*':
                a = int(st.pop())
                b = int(st.pop())
                st.append(a * b)

            elif token == '/':
                a = int(st.pop())
                b = int(st.pop())
                st.append(b / a)

            else:
                st.append(token)

        return int(st[0])



            