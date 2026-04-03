class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(" : ")",
                    "{" : "}",
                    "[" : "]"}

        stack = []

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack: return False
                popped = stack.pop()
                if brackets[popped] != c:
                    return False

        return not stack