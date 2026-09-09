class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == '+':
                st.append(st[-1] + st[-2])
            elif op == 'D':
                st.append(2 * st[-1])
            elif op == 'C':
                st.pop()
            else:
                st.append(int(op))

        return sum(st)

        # ["5","-2","4","C","D","9","+","+"]
        # [5, -2, -4, 9, 5, 14 ]
        # res = 27
