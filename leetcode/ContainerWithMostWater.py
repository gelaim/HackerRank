class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_water = 0
        left = 0
        right = len(height)-1
        
        while left <= right:
            
            smallest = min(height[left], height[right])
            max_water = max(max_water, smallest*(right-left))
            if smallest == height[left]:
                left +=1
            else:
                right -=1
        return max_water
        
        
        #for i in range(len(height)-1):
        #    for j in range(i+1, len(height)):
        #        smallest = min(height[i], height[j])
        #        max_water = max(max_water, smallest*(j-i))
        return max_water