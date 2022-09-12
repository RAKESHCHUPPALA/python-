from vehicle import vehicle

class car(vehicle):

    def car_model(self):
        print("car model is Benz")

    def Manufacture(self):
        print("Manufacture on 2000")
    def fuel_capacity(self):
        print("max fuel capacity for Benz is 40")


obj=car()
obj.car_model()
obj.Manufacture()
obj.colour()
obj.fuel_capacity()
obj.Max_speed()