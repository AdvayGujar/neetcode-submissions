class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()

        for index, num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()
            queue.append(num)

            if index >= k and nums[index - k] == queue[0]:
                queue.popleft()
            
            if index >= k-1:
                result.append(queue[0])

        return result