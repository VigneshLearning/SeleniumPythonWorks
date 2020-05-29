class Parent:
    def __init__(self):
        print("This is Parent Class")
    def ParFunc(self):
        print("This is Parent Function")
obj = Parent()
obj.ParFunc()

class Child(Parent):
    def __init__(self):
        print("This is Child Class")
    def ChildFunc(self):
        print("This is Child Function")
    #     THE BELOW IS METHOD OVER RIDING
    def ParFunc(self):
            print("This is Method Overiding")
obj1 = Child()
obj1.ChildFunc()
obj1.ParFunc()


