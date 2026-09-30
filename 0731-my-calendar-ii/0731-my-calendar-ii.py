class MyCalendarTwo:

    def __init__(self):
        self.events  ={}


        

    def book(self, startTime: int, endTime: int) -> bool:
        self.events[startTime] = self.events.get(startTime, 0) + 1
        self.events[endTime] = self.events.get(endTime, 0) - 1

        active = 0

        for time in sorted(self.events):
            active += self.events[time]

            if active >= 3:
                # Undo the booking
                self.events[startTime] -= 1
                self.events[endTime] += 1

                if self.events[startTime] == 0:
                    del self.events[startTime]

                if self.events[endTime] == 0:
                    del self.events[endTime]

                return False

        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)