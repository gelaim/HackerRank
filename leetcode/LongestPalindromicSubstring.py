class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        resultLenght = 0
        
        for i in range(len(s)):
            left = i
            right = i
            
            while left >=0 and right <len(s) and s[left]==s[right]:
                if len(s[left:right+1]) >= resultLenght:
                    result = s[left:right+1]
                    resultLenght = len(result)
                left -=1
                right +=1
            left = i
            right = i+1
            while left >=0 and right <len(s) and s[left]==s[right]:
                if len(s[left:right+1]) >= resultLenght:
                    result = s[left:right+1]
                    resultLenght = len(result)
                left -=1
                right +=1
                    
        return result 