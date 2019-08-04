""" Electrical car presentation \
    inherit class Car()
    
    Battery()
"""

import car

class Battery():
    """ Prosta próba modelowania akumulatora samochodu elektrycznego"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def descriptive_battery(self):
        """ Wyświetlanoe informacji o wielkości akumulatora"""
        print("Ten samochód ma akumulator o pojemności " + str(self.battery_size) + " kWh")

    def upgrade_battery(self, new_capacity):
        """ Symulacja wymiany akumulatora na większą pojemność"""
        if self.battery_size <= 70:
            self.battery_size = new_capacity
    
    def get_range(self):
        """ Wyświetla informację o zasięgu samochodu na podstawie pojemności akumulatora"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size > 70:
            range = (self.battery_size*240)/70

        message = "Zasięg samochodu wynosi około " +  f"{range:.3f}"
        message +=" km po pełnym naładowaniu akumulatora."
        print(message)


class ElectricCar(car.Car):
    """ Przedstawia cechy charakterystyczne dla samochodu elektrycznego"""

    def __init__(self, make, model, year):
        """ Inicjacja atrybutów klasy nadrzędnej"""
        super().__init__(make, model, year)
    
        self.battery = Battery()
