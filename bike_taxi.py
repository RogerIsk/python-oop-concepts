import os
os.system('clear')

from bike import Bike
from public_transport import PublicTransport

class BikeTaxi(Bike, PublicTransport):

    def __init__(self, motorized, **kwargs):
        self.maximum_mileage = kwargs.get("maximum_mileage", 600)
        self._scrap_metal = False
        self.motorized = motorized               # setting motorized to True
        self.speed = 18 if not motorized else 30 # setting speed to 18 if not motorized, else 30 - AI did this line
        self.passengers = 0
        self.distance_driven = 0

    def drive(self, km: int):    # it took me LONG to figure out that I need to put self.scrap_metal in the __init__ method
        return super().drive(km)

    def enter_passengers(self, count):
        if self.motorized == False and count < 2:
            if self.passengers + count > 2:
                print("The BikeTaxi is full. No more passengers can enter.")
                return
            self.passengers += count
            print(f"{count} passengers are entering. (Total passengers: {self.passengers})")
        elif self.motorized == True and count < 4:
            if self.passengers + count > 4:
                print("The BikeTaxi is full. No more passengers can enter.")
                return
            self.passengers += count
            print(f"{count} passengers are entering. (Total passengers: {self.passengers})")

    def exit_passengers(self, count):
        self.passengers -= count
        print(f"{count} passengers exited. (Total passengers: {self.passengers})")

    def get_current_passengers(self) -> int:
            return self.__current_passengers

    def repair(self):
        print("The BikeTaxi needs to be repaired before it can go any further.")
        print("The BikeTaxi has been repaired.")