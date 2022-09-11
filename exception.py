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
            intialvalue = intialvalue + 2
            if intialvalue == 300:
                continue
            print(intialvalue)

    def forlooop(self,intial,endvalue):
        fruits=["apple", "orange", "pineapple", "melon"]
        for eachvalue in fruits:
            print(eachvalue)
        for eachvalue1 in range(intial,endvalue):
            if eachvalue1 == 150:
               break
                print(eachvalue1)

    def div(self,number):
        try:
            a=10
            c=a/number
            print("The division of number is:",c)
        except:
            print("There is an exception")
        finally:
            print("finally is exception")




clsobj = classconcept()
clsobj.print100()
clsobj.div(0)
clsobj.printt()
clsobj.printtt(100)
clsobj.forloop(100,150)
clsobj.forlooop(100, 199)







