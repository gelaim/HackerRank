class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        xList = [int(y) for y in str(x)]
        left = 0
        right = len(xList)-1
        for i in range(len(xList)//2):
            if xList[left+i] == xList[right-i]:
                continue
            return False
        return True