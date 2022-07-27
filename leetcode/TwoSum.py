class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing not in adict:
                adict[nums[i]] = i
            else:
                return [i,adict[missing]]
        return [0]