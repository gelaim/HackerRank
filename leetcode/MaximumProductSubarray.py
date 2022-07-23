class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        cur_min, cur_max = 1,1
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_max = 1
                cur_min = 1
                max_prod = max(max_prod, 0)   
            else:
                aux = cur_max
                cur_max = max(nums[i], cur_min*nums[i], cur_max*nums[i])
                cur_min = min(nums[i], cur_min*nums[i], aux*nums[i])
                max_prod = max(max_prod, cur_max)   
            
        return max_prod