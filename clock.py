from datetime import datetime as dt
from timer import Timer
from alarm import Alarm

class Clock:
    __alarm_fnc = Alarm()
    __timer_fnc = Timer()

    __slots__ = ['__current_datetime', '__time_alarm']

    def __init__(self):
        self.__current_datetime = dt.now()
        self.__time_alarm = None
    
    def get_time(self):
        return f'{self.__current_datetime}'





