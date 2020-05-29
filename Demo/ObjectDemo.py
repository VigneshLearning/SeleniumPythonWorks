class TestDemo:
#     def add(self,name):
#         print("Calling add Function")
#         print(name)
#     def sub(self):
#         print("Calling sub function")
#
# obj = TestDemo()
# obj.add("Kanmani")
# obj.sub()
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    def callname(self):
        print("My name is "+self.name)
    def callage(self):
        print("My age is "+self.age)
obj1 = TestDemo("Smrithi","1")
obj1.callname()
obj1.callage()
print("")
obj2 = TestDemo("Abinitha","1")
obj2.callname()
obj2.callage()

