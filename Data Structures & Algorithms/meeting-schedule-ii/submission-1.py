"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        intervals.sort(key=lambda i: i.start)
        heap = [intervals[0].end]
        heapq.heapify(heap)
        rooms = 1

        for current in intervals[1:]:
            if current.start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, current.end)
            else:
                heapq.heappush(heap, current.end)
                rooms += 1

        return rooms