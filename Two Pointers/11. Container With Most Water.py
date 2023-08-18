class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        while right > left:
            if min(height[left], height[right]) * (right - left) > maxWater:
                maxWater = min(height[left], height[right]) * (right - left)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return maxWater
