from vehicle import Vehicle


class Bike(Vehicle):
    
    def __init__(self, motorized=False, **kwargs):
        kwargs["maximum_mileage"] = 600
        self._mileage_until_next_repair = 200
        kwargs['motorized'] = motorized
        if "speed" not in kwargs:
            kwargs["speed"] = 20
        super().__init__(**kwargs)
        

    def repair(self):
        print("The "
        + type(self).__name__
        + " has been repaired.")
        self._mileage_until_next_repair = 200

    def drive(self, km: int):
        return super().drive(km)
