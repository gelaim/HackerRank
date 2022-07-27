class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        left = 0
        curr_max = nums[left]
        for i in range(len(nums)):
            if nums[i] > nums[left]:
                left +=1
                nums[left] = nums[i]
                k+=1
        return k