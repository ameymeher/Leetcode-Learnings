from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.data = SortedList()

    def book(self, start: int, end: int) -> bool:

        i = self.data.bisect_right((start,end))

        if (i>0 and self.data[i-1][1] > start) or (
            i < len(self.data) and self.data[i][0] < end
        ):
            return False

        self.data.add((start,end))
        return True
            


            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)