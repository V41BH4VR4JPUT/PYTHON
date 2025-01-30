# Super keyword in Python
class parent:
    def Parent_method(self):
        print("This is parent class method")
class child(parent):
    def child_method(self):
        print("This is child class method")
        super().Parent_method()
c=child()
c.child_method()