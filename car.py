""" Class Car: car presentation \
        mark, model, year
"""


class Car():
    """ Prosta próba zaprezentowania samochodu """

    def __init__(self, make, model, year):
        """ Inicjalizacja  atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """ Wyświetla informację o przebiegu samochodu"""
        print("Ten samochód ma przejechane " + str(self.odometer_reading) + " km.")

    def update_odometer(self, mileage):
        """ Przypisanie nowej wartości licznikowi przebiegu"""
        self.odometer_reading = mileage

    def incremwnt_odometer(self, kilometers):
        """ Inkrementacja wartości licznika przebiegu samochodu o podaną wartość"""
        self.odometer_reading += kilometers

