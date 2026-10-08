class Clock:
    # Служебные методы, если нужны
    
    def __init__(self):
        self.minutes = 0
        self.hours = 0

    # Передвинуть время вперёд на minutes минут. Если minutes отрицательное - выбросить exception.
    def tick(self, minutes):
        if(minutes <0):
            print(1/0)
        self.minutes += minutes

    # Вернуть текущее время как tuple из часов и минут.
    def get_time(self):
        return("(" + str( (self.minutes)//60 % 24) + ", " + str((self.minutes)%60) + ")")

c = Clock()
print(c.get_time())
c.tick(60*23 + 15)
print(c.get_time())
