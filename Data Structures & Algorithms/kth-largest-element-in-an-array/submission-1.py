class Solution:
    def findKthLargest(self, nums, k):
        maxHeap = [-s for s in nums]
        heapq.heapify(maxHeap)
        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1
            if k == 0:
                return -res 