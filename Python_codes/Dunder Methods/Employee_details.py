class Employee:
    def __init__(self , name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"{self.name} is {self.age} years old and earns {self.salary} per month"
    def __repr__(self):
        return f"Employee('{self.name}' , {self.age} , {self.salary})"
    def __call__(self):
        print(f"{self.name} is a capable employee")