"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)

        lastEnd = -1

        for i in intervals:
            start, end = i.start, i.end
            if start < lastEnd:
                return False
            else:
                lastEnd = end
        return True
