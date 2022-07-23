class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        adict = {}
        for i in range(len(nums)):
            if nums[i] in adict:
                return True
            else:
                adict[nums[i]]=True
        return False
        