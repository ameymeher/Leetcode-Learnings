"""
For a input of list, this solution is efficient.
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = list(map(lambda x: int(x[:2])*60 + int(x[3:]),timePoints))

        timePoints.sort()

        ans = min(timePoints[i+1] - timePoints[i] for i in range(len(timePoints)-1))

        return min(ans, 24*60 - timePoints[-1] + timePoints[0])

"""
For a input of stream, this solution is efficient.
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        bucket = [False] * (24 * 60)

        for time in timePoints:
            minutes = int(time[:2]) * 60 + int(time[3:])
            if bucket[minutes]:
                return 0
            bucket[minutes] = True

        first, prev, min_diff = None, None, float('inf')

        for i, present in enumerate(bucket):
            if present:
                if first is None:
                    first = i
                if prev is not None:
                    min_diff = min(min_diff, i - prev)
                prev = i

        min_diff = min(min_diff, (24 * 60 - prev + first))

        return min_diff