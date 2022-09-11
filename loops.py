class classconcept():

    def print100(self):
        print(1)
        print(2)
        print(3)
        print(4)

    def printt(self):
        intialvalue=1
        endvalue=10000

        while intialvalue<=100:
            print(intialvalue)
            intialvalue=intialvalue+1

    def printtt(self,intialvalue,endvalue):
        while intialvalue <= endvalue:
            print(intialvalue)
            intialvalue=intialvalue+1

    def forlooop(self,intial,endvalue):
        fruits = ["apple", "orange", "pineapple", "melon"]
        for eachvalue in fruits:
            print(eachvalue)
        for eachvalue in range(1,4):
            print(eachvalue)

clsobj=classconcept()
clsobj.print100()
clsobj.printt()
clsobj.printtt(100,500)
clsobj.forloop()
clsobj.forlooop(100,199)


