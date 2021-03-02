from time import time


class StopWatch:
    startTimer = 0
    stopTimer = 0
    elapsed = 0

    def start(self):
        """function to calculating start time in milliseconds"""
        self.startTimer = int(time() * 1000)
        print("Start Time", self.startTimer)

    def stop(self):
        """function to calculating stop time in milliseconds"""
        self.startTimer = int(time() * 1000)
        print("stop Time", self.stopTimer)

    def getElapsed(self):
        """function to get elapsed time
        :return: returns the elapsed time"""
        self.elapsed = self.stopTimer - self.startTimer
        return self.elapsed


class ValueNotEqualError(Exception):
    """raised when the input value is too small"""
    pass


watch = StopWatch()
value = 1
while value == 1:
    try:
        userInput = int(input("press 1 to start time"))
        if userInput != 1:
            raise ValueNotEqualError
        watch.start()  # function call to start times
        print()

        userInput = int(input("press 2 to stop time"))
        if userInput != 2:
            raise ValueNotEqualError
        watch.stop()  # function call to stop timer
        print()

        elapsed = watch.getElapsed()  # function call to get elapsed time after stopping the timer
        print("Total time Elapsed(in seconds) is", int(elapsed / 1000))  # print elapsed time in seconds
        break
    except ValueNotEqualError:
        print("Enter 1 to start timer and 2 to stop timer")
