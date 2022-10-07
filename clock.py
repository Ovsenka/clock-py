from timer import Timer
from alarm import Alarm, dt

class Clock:

    _alarm = Alarm()
    _timer = Timer()

    def __init__(self):
        self.__current_datetime = dt.now()
        self.__time_alarm = None
    
    def get_time(self):
        return f'{self.__current_datetime}'

    
    def start_timer(self):
        self._timer.start()
        print("Timer started!")
    
    def stop_timer(self):
        self._timer.stop()
        print("Timer stopped!")





