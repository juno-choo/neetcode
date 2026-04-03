class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(opn, cls):
            if opn == cls == n:
                res.append(''.join(stack.copy()))
                return

            if opn < n:
                stack.append("(")
                dfs(opn + 1, cls)
                stack.pop()
            if opn > cls:
                stack.append(")")
                dfs(opn, cls + 1)
                stack.pop()
            
        dfs(0,0)
        return res


