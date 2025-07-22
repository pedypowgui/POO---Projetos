class WeekDayError(Exception):
    pass

class Weeker:
    def __init__(self, day):
        self.__days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        if day not in self.__days:
            raise WeekDayError()
        self.__day = day
            
    def __str__(self):
        return self.__day #Transformando em string para poder imprimir os valores
        
    def add_days(self, n):
        index = self.__days.index(self.__day)
        new_index = (index + n) % 7 #Simplifica o número do dia da semana para facilitar o uso da lista
        self.__day = self.__days[new_index]

    def subtract_days(self, n):
        index = self.__days.index(self.__day)
        new_index = (index - n) % 7 #Mesmo processo do add_days só que para subtrair os dias
        self.__day = self.__days[new_index]

#Testes para verificar funcionalidade do programa
try:
    weekday = Weeker('Mon')
    print(weekday)

    weekday.add_days(15)
    print(weekday)

    weekday.subtract_days(23)
    print(weekday)

    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    
