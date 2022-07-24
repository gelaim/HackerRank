class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = set()
        
        for i in range(len(nums)-2):
            first = i
            second = i+1
            third = len(nums)-1
            while second < third:
                num_1 = nums[first]
                num_2 = nums[second]
                num_3 = nums[third]
                if num_1 + num_2 + num_3 == 0:
                    result.add((num_1,num_2,num_3))
                
                if num_1 + num_2 + num_3 > 0:
                    third -=1
                else:
                    second +=1

        return result