class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftPointer = 0
        rightPointer = len(height)-1
        leftMax = height[leftPointer]
        rightMax = height[rightPointer]
        water = 0

        while leftPointer < rightPointer:
            if leftMax < rightMax:
                leftPointer += 1
                leftMax = max(leftMax, height[leftPointer])
                water += leftMax - height[leftPointer]
            else:
                rightPointer -= 1
                rightMax = max(rightMax, height[rightPointer])
                water += rightMax - height[rightPointer]
        
        return water