class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"(":")", "[":"]", "{":"}"}
        stack = []
        for char in s:
            if char in dict:
                stack.append(char)
            else:
                if stack == [] or dict[stack.pop()] != char:
                    return False 
            
        return True if stack == [] else False