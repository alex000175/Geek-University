# 1. Светофор

import time

class TrafficLight():
    time_red = 7
    time_yellow = 2
    time_green = 10
    stop_cycle = 2

    def __init__(self, color):
        self.color = color

    def running(self):
        if self.color == 'red':
            self.__turn_to_red()
        elif self.color == 'yellow':
            self.__turn_to_yellow()
        elif self.color == 'green':
            self.__turn_to_green()
        else:
            print('Укажите в конструкторе в качестве параметра стартовый цвет светофора: red yellow или green')

    def __turn_to_red(self):
        self.color = 'red'
        timer = time.perf_counter()
        while time.perf_counter() < timer + self.time_red:
            for p in range(self.time_red):
                print(f"\033[91m\rred {p}", end="", flush=True)
                time.sleep(1)
        self.__turn_to_yellow()

    def __turn_to_yellow(self):
        self.color = 'yellow'
        timer = time.perf_counter()
        while time.perf_counter() < timer + self.time_yellow:
            for p in range(self.time_yellow):
                print(f"\033[93m\ryellow {p}", end="", flush=True)
                time.sleep(1)
        self.__turn_to_green()

    def __turn_to_green(self):
        self.color = 'green'
        timer = time.perf_counter()
        self.stop_cycle -= 1
        while time.perf_counter() < timer + self.time_green:
            for p in range(self.time_green):
                print(f"\033[92m\rgreen {p}", end="", flush=True)
                time.sleep(1)
        if self.stop_cycle == 0:
            return
        self.__turn_to_red()


# ---------------------------------------------------------------------------------
a = TrafficLight('red')

# a.time_red = 7 # продолжительность первого состояния (сек)
# a.time_yellow = 2 # продолжительность второго состояния (сек)
# a.time_green = 5 # продолжительность троетьего состояния (сек)
# a.stop_cycle = 5 # остановка через указанное количество циклов

a.running()
