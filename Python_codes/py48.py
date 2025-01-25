# class variable and instance variable
"""  Class Variable """
# class m():
#     c_m = 0
#     def __init__(self):
#         m.c_m += 1
#     def print_m(self):
#         print(m.c_m)

# o1 = m()
# o1.print_m()
# o2 = m()
# o2.print_m()

"""  Instance Variable """
class i():
    def __init__(self , name):
        self.name = name 
    def print_name(self):
        print(self.name)

o1 = i("John")
o1.print_name()
o2 = i("Doe")
o2.print_name()
