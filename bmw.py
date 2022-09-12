from Ferrari import*

class bmw:

     def fuel_type(self):
         print("diesel")

     def max_speed(self):
         print("Max speed is 240")



"""obj=bmw()
obj.fuel_type()
obj.max_speed()
obj1.fuel_type()
obj1.max_speed()
obj1=Ferrari()"""

for eachobj in (bmw(),Ferrari()):
    eachobj.fuel_type()
    eachobj.max_speed()