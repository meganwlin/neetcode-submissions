class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(result, n):
            if len(result) == n * 2:
                answer.append(result)
            else:
                openCount = result.count("(")
                if openCount == n:
                    result += ")"
                    dfs(result, n)
                else:
                    result += "("
                    dfs(result, n)
                    # if the number of preceding open parentheses is less than current closed parentheses
                    result=result[:-1]
                    if (result.count(")") < result.count("(")):
                        result += ")"
                        dfs(result, n)
        
        dfs("(", n)
        return answer
        
