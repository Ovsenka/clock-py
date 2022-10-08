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

    @staticmethod
    def clear():
        system('clear')

    def mainloop(self):
        while True:
            print("--- Clock ---")
            print("Current time: {}".format(
                strformat(self.get_time()))
            )
            sleep(1)
            self.set_time(dt.now())
            self.clear()

        


