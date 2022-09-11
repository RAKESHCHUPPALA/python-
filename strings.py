class stringconcept():

    def stringhandle(self):
        name="rakesh kumar"
        company='SAI RAMGEETH ENTERPRISES'
        filename="rakesh.xlxs"
        print(name)
        print(company)
        for each in range(0,len(name)):
            print(name[each])
        totalcharacter=len(name)
        print(totalcharacter)
        rakeshexist= "rakesh" in name
        print(rakeshexist)
        count=0
        for each in range(0, len(name)):
            if (name[each])=='Z':
                count+=1
            print("the given r present this many time",count)
            rakeshdoesnotexist = "rakesh" not in name
            print(rakeshdoesnotexist)
            #specific position value
            totllen=len(filename)
            actualvalue=filename[0:totllen]
            print(filename[len(name)-4:len(name)])
            print(filename.upper())
            print(name)
            print(name.strip())
            print(name.lstrip())
            print(name.rstrip())
            print(name.replace("kumar","k"))
            print(name.split("a"))
            print(name.split(' ' ))
            print(name+company)
            testindoublecoats="rakesh \"kumar\""
            print(testindoublecoats)
            print(filename.count("r"))
            print(filename.startswith("rakesh"))
            print(filename.endswith("kumar"))
            characterposition=filename.rfind(" , ")
            print(filename[characterposition+1:len(filename)])
            print(filename.reverse())






obj=stringconcept()
obj.stringhandle()