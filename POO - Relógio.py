import time
from datetime import datetime
import os

def formatar(val): # formatar os zeros na contagem
    return f"{val:02}"

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__h = hours
        self.__m = minutes
        self.__s = seconds

    def __str__(self):
        return f"{formatar(self.__h)}:{formatar(self.__m)}:{formatar(self.__s)}"

    def next_second(self): #Adicionar 1 segundo
        if self.__s < 59:
            self.__s += 1
        else:
            self.__s = 0
            self.__m += 1
            if self.__m == 60:
                self.__m = 0
                self.__h += 1
                if self.__h == 24:
                    self.__h = 0

agora = datetime.now()
timer = Timer(agora.hour, agora.minute, agora.second)

while True:
    print(timer)
    timer.next_second()
    time.sleep(1)
    os.system('cls')
