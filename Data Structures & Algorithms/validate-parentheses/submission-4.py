class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in d:
                # It is an opening bracket so we append
                stack.append(bracket)
            else:
                if not(stack and bracket == d[stack.pop()]):
                    return False
        return not stack