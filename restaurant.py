""" Klasa Restaurant """
class Restaurant():
    """Simple restaurant info: restaureant_name, cuisine_type """
    def __init__(self, restaurant_name, cuisine_type):
        """ Inicjacja atrybutów klasy Restaurant """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Wyświetla opis restauracji"""
        print("Nazwa restauracji:" + self.restaurant_name)
        print("Profil podawanych dań: " + self.cuisine_type)

    def open_restaurant(self):
        """ Wyświetla godziny otwarcia restauracji """
        print("Poniedziałek: ".ljust(12) + "17-23")
        print("Wtoek: ".ljust(12) +  "17-23")
        print("Środa: ".ljust(12) +  "17-23")
        print("Czwartek: ".ljust(12) +  "17-23")
        print("Piątek: ".ljust(12) +  "17-23")
        print("Sobota: ".ljust(12) +  "17-24")
        print("Niedziela: ".ljust(12) + "17-24")

    def set_number_served(self, number_served):
        self.number_served = number_served