class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]
        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            cur = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, cur)
            heapq.heappush(heap, (-cur, i))
        return ans