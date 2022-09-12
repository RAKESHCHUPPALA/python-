from vehicle import vehicle

class bike(vehicle):

    def manufactured(self):
        print("Manufactured on 2022")

    def Model(self):
        print("Activa 3g")


    def Max_speed(self):
        print("Max speed should be 80")



obj=bike()
obj.manufactured()
obj.Model()
obj.colour()
obj.Max_speed()