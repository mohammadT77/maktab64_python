from datetime import datetime
from time import sleep


class ProcessTimer:
    __start_time: datetime
    __end_time: datetime

    def __enter__(self):
        self.__start_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__end_time = datetime.now()

    @property
    def elapsed_time(self):
        return self.__end_time - self.__start_time


ptimer = ProcessTimer()
with ptimer:
    sleep(2)

print(ptimer.elapsed_time)
