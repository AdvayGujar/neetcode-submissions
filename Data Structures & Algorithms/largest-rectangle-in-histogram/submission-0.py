class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = deque()

        leftMax = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMax[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMax = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMax[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            left = leftMax[i] + 1
            right = rightMax[i] - 1
            maxArea = max(maxArea, heights[i] * (right - left + 1))

        return maxArea 