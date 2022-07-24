class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        middle = right//2
        
        if len(nums) <=2:
            return min(nums)
        
        
        while left != right != middle:
            if nums[middle-1] > nums[middle]:
                return nums[middle]
            
            if nums[left] < nums[right]:
                return nums[left]
            if nums[middle] >= nums[left]:
                left = middle+1
            else:
                right = middle -1
            middle = (right - left)//2 + left
        return nums[middle]