class MyCalendarThree:

    def __init__(self):
        self.events = {}


    def book(self, startTime: int, endTime: int) -> int:
        self.events[startTime] = self.events.get(startTime, 0) + 1
        self.events[endTime] = self.events.get(endTime, 0) - 1

        active = 0
        max_overlap = 0

        for time in sorted(self.events):
            active += self.events[time]
            max_overlap = max(max_overlap, active)

        return max_overlap


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)