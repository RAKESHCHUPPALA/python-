class classconcept():

    global tax
    tax=0.4

    def incometax(self,income):
        if(income<1000):
            self.tax=.1
            taxtopercentagure=income*self.tax
            taxcal=income+taxtopercentagure
            print("with in 1000: "+str(taxcal))

        else:
            taxtopercentagure = income * tax
            taxcal= income + taxtopercentagure
            print(taxcal)




clsobj=classconcept()
clsobj.incometax(1500)