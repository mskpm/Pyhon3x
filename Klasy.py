# Będziemy ćwiczyć klasy w Python'nie

#9.1, 9.4, 9.10
#class Restaurant():
#    """Simple restaurant info: restaureant_name, cuisine_type """
#    def __init__(self, restaurant_name, cuisine_type):
#        """ Inicjacja atrybutów klasy Restaurant """
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#        self.number_served = 0

#    def describe_restaurant(self):
#        """ Wyświetla opis restauracji"""
#        print("Nazwa restauracji:" + self.restaurant_name)
#        print("Profil podawanych dań: " + self.cuisine_type)

#    def open_restaurant(self):
#        """ Wyświetla godziny otwarcia restauracji """
#        print("Poniedziałek: ".ljust(12) + "17-23")
#        print("Wtoek: ".ljust(12) +  "17-23")
#        print("Środa: ".ljust(12) +  "17-23")
#        print("Czwartek: ".ljust(12) +  "17-23")
#        print("Piątek: ".ljust(12) +  "17-23")
#        print("Sobota: ".ljust(12) +  "17-24")
#        print("Niedziela: ".ljust(12) + "17-24")

#    def set_number_served(self, number_served):
#        self.number_served = number_served

# 9.10
#import restaurant

#my_restaurant = restaurant.Restaurant("Picolo", "Kuchnia sycylijska")
#my_restaurant.describe_restaurant()

#9.6

#class IceCreamStand(Restaurant):
#    """  class inherited by Restaurant """
#    def __init__(self, restaurant_name, cuisine_type):
#        """  Initialize parent class """
#        super().__init__(restaurant_name, cuisine_type)
#        self.flavours = "vanilla"
    
#    def show_flovour(self):
#        """ Prints ice cream flovour """
#        print("Ice stand serves: " + str(self.flavours))


#my_ice = IceCreamStand("Lodi", "kręcone")

#my_ice.show_flovour()
#my_ice.set_number_served(10)
#print(str(my_ice.number_served))
#print(str(my_ice.cuisine_type))


#my_restaurant = Restaurant("U Piotra", "Domowe żarcie")
#my_restaurant.set_number_served(10)
#print("Obsłużonych gości: " + str(my_restaurant.number_served))
#print(my_restaurant.restaurant_name)
#print(my_restaurant.cuisine_type)
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

#9.2

#restaurant1 = Restaurant("Picolo", "Kuchnia sycylijska")
#restaurant2 = Restaurant("Pari-Pari", "Kuchnia francuska")
#restaurant3 = Restaurant("Chłopskie Jadło", "Kuchnia polska")

#restaurant1.describe_restaurant()
#restaurant2.describe_restaurant()
#restaurant3.describe_restaurant()

#9.3, 9.5

#class User():
#    """ User data """
#    def __init__(self, first_name, middle_name, last_name, home_dir):
#        self.first_name = first_name
#        if middle_name:
#            self.middle_name = middle_name
#        else:
#            self.middle_name = ""
#        self.last_name = last_name
#        self.home_dir = home_dir
#        self.login_attempts = 0

#    def describe_user(self):
#        print(self.first_name)
#        print(self.middle_name)
#        print(self.last_name)
#        print(self.home_dir)
#        print(self.login_attempts)
    
#    def increment_login_attempts(self):
#        """ Increments login attempts for 1 """
#        self.login_attempts += 1

#    def reset_login_attempts(self):
#        """ Reset login attempts to 0 """
#        self.login_attempts = 0

#    def great_user(self):
#        if self.middle_name:
#            print("\nWitaj " + str(self.first_name).title() + " " + str(self.middle_name).title() + " " + str(self.last_name).title() +"!")
#        else:
#            print("\nWitaj " + str(self.first_name).title() + " " + str(self.last_name).title() + "!")

#        print("Twój katalog domowy to: " + str(self.home_dir))
#        print("Zanotowano prób logoania: " + str(self.login_attempts))

#userx = User('Piotr', 'Marcin', 'Majkowski', '/home/users/majkowsp')
#usery = User('Robert', '', 'Wiernicki', '/home/users/wiernicr')

#userx.increment_login_attempts()
#print("Liczba logowań: " + str(userx.login_attempts))
#userx.reset_login_attempts()
#print("Reset liczby logowań")
#print("Liczba logowań: " + str(userx.login_attempts))

#userx.describe_user()
#userx.great_user()
#usery.describe_user()
#usery.great_user()

# 9.7, 9.8

#class Privileges():
#    """ Class with atribute 'privileges'"""
#    privileges = ["może coś więcej", "może ale nie musi", "patrzy w dobą stronę"]

#    def show_privileges(self):
#        """ Prints Admin privileges"""
#        print("\nAdmin privileges: \n")
#        for privilege in self.privileges:
#            print("\t" + privilege + ", ")


#class Admin(User):
#    """ class inherits from User """
#    def __init__(self, first_name, middle_name, last_name, home_dir):
#        return super().__init__(first_name, middle_name, last_name, home_dir)
#    #privileges = ["może coś więcej", "może ale nie musi", "patrzy w dobą stronę"]
#    privileges = Privileges()

    #def show_privileges(self):
    #    """ Prints Admin privileges"""
    #    print("\nAdmin privileges: \n")
    #    for privilege in self.privileges:
    #        print("\t" + privilege + ", ")

#my_admin = Admin('Piotr', 'Marcin', 'Majkowski', '/home/users/majkowsp')
#print(str(my_admin.privileges))
#my_admin.show_privileges()

#my_admin1 = Admin('Piotr', 'Marcin', 'Majkowski', '/home/users/majkowsp')
#my_admin1.privileges.show_privileges()


#9.11
#import user

#my_admin = user.Admin('Piotr', 'Marcin', 'Majkowski', '/home/users/majkowsp')
#my_admin.privileges.show_privileges()

##9.12
#import admin

#my_admin = admin.Admin('Piotr', 'Marcin', 'Majkowski', '/home/users/majkowsp')
#my_admin.privileges.show_privileges()




#9.9

#class Car():
#    """ Prosta próba zaprezentowania samochodu """

#    def __init__(self, make, model, year):
#        """ Inicjalizacja  atrybutów opisujących samochód"""
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0

#    def get_descriptive_name(self):
#        """ Zwrot elegancko sformatowanego opisu samochodu"""
#        long_name = str(self.year) + " " + self.make + " " + self.model
#        return long_name

#    def read_odometer(self):
#        """ Wyświetla informację o przebiegu samochodu"""
#        print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km.")

#    def update_odometer(self, mileage):
#        """ Przypisanie nowej wartości licznikowi przebiegu"""
#        self.odometer_reading = mileage

#    def incremwnt_odometer(self, kilometers):
#        """ Inkrementacja wartości licznika przebiegu samochodu o podaną wartość"""
#        self.odometer_reading += kilometers

#class Battery():
#    """ Prosta próba modelowania akumulatora samochodu elektrycznego"""
#    def __init__(self, battery_size = 70):
#        self.battery_size = battery_size

#    def descriptive_battery(self):
#        """ Wyświetlanoe informacji o wielkości akumulatora"""
#        print("Ten samochód ma akumulator o pojemności " + str(self.battery_size) + " kWh")

#    def upgrade_battery(self, new_capacity):
#        """ Symulacja wymiany akumulatora na większą pojemność"""
#        if self.battery_size <= 70:
#            self.battery_size = new_capacity
    
#    def get_range(self):
#        """ Wyświetla informację o zasięgu samochodu na podstawie pojemności akumulatora"""
#        if self.battery_size == 70:
#            range = 240
#        elif self.battery_size > 70:
#            range = (self.battery_size*240)/70

#        message = "Zasięg samochodu wynosi około " +  f"{range:.3f}"
#        message +=" km po pełnym naładowaniu akumulatora."
#        print(message)

#class ElectricCar(Car):
#    """ Przedstawia cechy charakterystyczne dla samochodu elektrycznego"""

#    def __init__(self, make, model, year):
#        """ Inicjacja atrybutów klasy nadrzędnej"""
#        super().__init__(make, model, year)
    
#        self.battery = Battery()

import car    

my_car = car.Car("Opel", "Astra H", 2006)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(100)

import car_electrical

my_car.read_odometer()
my_electric_car = car_electrical.ElectricCar("Opel", "Astra H", 2006)
my_electric_car.battery.descriptive_battery()
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery(100)
my_electric_car.battery.descriptive_battery()
my_electric_car.battery.get_range()
