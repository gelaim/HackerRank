class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)*(len(nums)+1)/2
        result = s -sum(nums)
        return int(result)