from timer import Timer
from alarm import Alarm, dt
from formatter import tformat, strformat
from time import sleep
from os import system

class Clock:

    _alarm = Alarm()
    _timer = Timer()

    def __init__(self):
        self.__current_datetime = dt.now()
    
    def get_time(self) -> dt:
        return self.__current_datetime

    def set_time(self, datetime: dt) -> None:
        self.__current_datetime = datetime
    
    def start_timer(self):
        self._timer.start()
        print("Timer started!")
    
    def stop_timer(self):
        self._timer.stop()
        print("Timer stopped!")

    def set_alarmt(self, datetime: dt):
        self._alarm.set_alarm(datetime)

    def get_alarmt(self) -> dt:
        return self._alarm.get_alarm()


    def is_alarm(self) -> bool:
        """Check if time for call alarm"""
        if self.get_alarmt() is not None:
            return self.compare(self.get_time(), self.get_alarmt())
        return False

    @staticmethod
    def compare(dt1: dt, dt2: dt) -> bool:
        if dt1.year == dt2.year and dt1.month == dt2.month and \
                dt1.day == dt2.day and dt1.hour == dt2.hour and dt1.minute == dt2.minute:
            return True
        return False
    @staticmethod
    def clear():
        system('clear')

    def mainloop(self):
        while True:
            print("--- Clock ---")
            print("Current time: {}".format(
                strformat(self.get_time()))
            )
            if self.is_alarm():
                print("BUZZZZ!!! Time for wake UP! Time: {}".format(strformat(self.get_time())))

            sleep(1)
            self.set_time(dt.now())
            self.clear()

        


