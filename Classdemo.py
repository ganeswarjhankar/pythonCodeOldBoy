class calculator:
    num = 100

# default Constructors

    def __init__(self,a,b):
        self.firstnumber= a
        self.secondnumber= b
        print("i am called automatically when object is created")


    def getData(self):
        print("Now i am executing as methods in class")

    def summation(self):







obj = calculator(2,3)
obj.getData()
print(obj.num)

obj1 = calculator(4,5)
obj1.getData()
print(obj1.num)

