class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        adict = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }
        strLen = len(digits)
        result = []
        listDigits = [int(x) for x in digits]
        def dfs(currDigits,value):
            if len(currDigits) == 0:
                result.append(value)
                return
            
            for v in adict[currDigits[0]]:
                dfs(currDigits[1:], value+v)
        dfs(listDigits,'')
        
        return result