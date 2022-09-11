class classconcept():
    def assignmentoperator(self):
        a=10
        b=10
        fruits=["apple","bannana","orange"]
        print("initial value: " + str(a))
        a=a+5
        print("after a addition of 5 is " + str(a))
        print(a == b)#comparative
        print(a != b)
        print(a>=b)
        print(a>10 and b<10)#logical
        print(not(a>10 and b<10))
        print(a>10 or b>=10)
        print("apple in fruits")

clsobj=classconcept()
clsobj.assignmentoperator()