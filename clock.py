from datetime import datetime as dt

class Clock:


    __slots__ = ['__current_datetime', '__time_alarm']

    def __init__(self):
        self.__current_datetime = dt.now()
        self.__time_alarm = None
    
    def get_time(self):
        return f'{self.__current_datetime}'





