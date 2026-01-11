class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area1 = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area2 = w * h
            area1 = max(area1, area2)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area1
    
# beats - 88.97%