class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        pairs = {"{":"}", "[" : "]", "(": ")"}

        for bracket in s:
            if bracket in pairs:
                # opening bracket found
                stack.append(bracket)
            else:
                # closing bracket
                if not stack:
                    return False
                opening = stack.pop()
                if pairs[opening] != bracket:
                    return False
        if len(stack) == 0:
            return True
        return False