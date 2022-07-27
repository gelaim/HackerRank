class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []
        
        def findSolutions(nOpens, nCloses):
            if nOpens == nCloses == n:
                result.append(''.join(current))
                return
            if nOpens < n:
                current.append('(')
                findSolutions(nOpens+1, nCloses)
                current.pop()
            
            if nOpens > nCloses:
                current.append(')')
                findSolutions(nOpens, nCloses+1)
                current.pop()

        findSolutions(0,0)

        return result  