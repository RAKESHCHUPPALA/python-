class Methodoverloading():

    def add(self):
        c=10+5
        print(c)

    def add(self,a,b):
        c=a+b
        print(c)


obj=Methodoverloading()
obj.add(3,2)

