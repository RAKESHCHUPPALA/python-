class classconcept():

    def ifcondition(self,age,country):
        if age>=18 and country=="IND":
            print("you are eligible to apply voter id")
        if age>=60:
            print("you are eligible for senior consession")
        if age>=80:
            print("you are eligible for super senior consession")
        elif age>15:
            waitperiod= 18 - age
            print("you are eligible for prevoter id. but to get an actual voter id you have to wait for " +str(waitperiod) + "")
        elif age>12:
            waitperiod = 18 - age
            print("you are eligible for pre voter id. but to get an actual voter id you have to wait for " + str(waitperiod) + "")
        else:
            waitperiod=18-age
            print("you are not eligible to apply voter id . please wait for " +str(waitperiod)+" more years")

    def gender(self,gendervalue):

        actualgender =""

        if gendervalue == "F":
                print("you are female")
                actualgender="female"
        elif gendervalue == "M":
                actualgender="male"
                print("you are male")

        elif gendervalue == "T":
                actualgender="transgender"
                print("you are transgender")

        else:
                print("this key word is not recognized . please give F , M or T")
        return actualgender
    def genderidentification(self,genderkeyword):
        actualgendername=clsobj.gender(genderkeyword)
        print(actualgendername)









clsobj=classconcept()
clsobj.ifcondition(15,"PAK")
clsobj.gender("M")
clsobj.genderidentification("M")

