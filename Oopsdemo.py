#self keyword is mandatory for calling the variables names into the method
#instance and class variables have whole different purpose
#constructor name should be  __init__
#new keyword is not reqiored when you create object


class calculator:
    num = 100


    def getData(self):
        print("I am now executing as method in Class")


obj = calculator()
# syntax to create object in Python
obj.getData()
#call the method
print(obj.num)

