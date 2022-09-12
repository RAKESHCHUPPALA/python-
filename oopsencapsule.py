class Encapsulation:

    global c
    c=20
    a=10
    _petrolcapacity = 20
    __maxspeed = 0
    __name = ""

    def __int__(self):
        pass
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "supercar"

    def drive(self):
        print('driving. maxspeed' + str(self.__maxspeed))

    def accessmodifier(self):
        print("the petrol capacity is: ",self._petrolcapacity)
        print("the a value is ": ",self.a)



redcar = Encapsulation()
redcar.drive()
#redcar.setMaxspeed(320)
redcar.drive()