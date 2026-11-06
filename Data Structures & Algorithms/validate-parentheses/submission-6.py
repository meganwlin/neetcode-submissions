class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        for char in s:
            if char in pairs.keys():
                stack.append(char)
            elif char in pairs.values():
                if not stack:
                    return False
                top = stack.pop()
                if top not in pairs.keys() or pairs[top]!= char:
                    return False
            else:
                return False
        return len(stack) == 0
        