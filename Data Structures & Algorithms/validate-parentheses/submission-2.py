class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in '(':
                stack.append(')')
            elif c in '[':
                stack.append(']')
            elif c in '{':
                stack.append('}')
            
            elif not stack or stack.pop() != c:
                return False
        return len(stack) == 0