import time
from exceptions import TimerError

class Timer():
    def __init__(self):
        self.__start_time = None

    def start(self) -> None:
        """Start timer"""
        if self.__start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self.__start_time = time.perf_counter()
    
    def stop(self) -> None:
        """Stop timer and report elapsed time"""
        if self.__start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")
        
        elapsed_time = time.perf_counter() - self.__start_time
        self.__start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
