# inhertance in python

class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name: %s, Age: %s, Salary: %s" % (self.name, self.age, self.salary))

class manager(employee):
    def __init__(self, name, age, salary, project):
        super().__init__(name, age, salary)
        self.project = project

    def display(self):
        print("Name: %s, Age: %s, Salary: %s, Project: %s" % (self.name, self.age, self.salary, self.project))

emp = employee("Vaibhav", 22, 50000)
emp.display()

mgr = manager("Vaibhav", 22, 50000, "Python")
mgr.display()
