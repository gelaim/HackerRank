class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float('-inf')
        curr = float('-inf')
        for i in range(len(nums)):
            if nums[i]>= curr:
                if curr >= 0:
                    curr+= nums[i]
                    max_sub = max(max_sub, curr)
                else:
                    curr = nums[i]
                    max_sub = max(max_sub, curr)
            elif nums[i] + curr >= 0:
                curr += nums[i] 
                max_sub = max(max_sub, curr)
            else:
                curr = nums[i]
        return max_sub    