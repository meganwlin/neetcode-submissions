"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)

        last_end = -1
        for i in sorted_intervals:
            if i.start < last_end:
                return False
            last_end = i.end
        return True


        