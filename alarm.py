from datetime import datetime as dt

class Alarm():
    def __init__(self, datet: dt = None):
        self.__current_alarm = datet

    def set_alarm(self, datetime: dt):
        self.__current_alarm = datetime

    def get_alarm(self) -> dt:
        return self.__current_alarm
    