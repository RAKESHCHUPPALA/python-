class classconcept():
    global a
    a=50
    b=20
    def studentdetails(self):
        self.a= 30
        self.b=20
        b=70
        print(self.a)
        print(self.b)
        print(a)
        print(b)
clsobj=classconcept()#
clsobj.studentdetails()
