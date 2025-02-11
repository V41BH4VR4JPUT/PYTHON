# Generators in python

def my_generator():
    for i in range(5):
        yield i

g = my_generator()
print(g)
# to print one value
print(next(g))
# to print all values in loop
for j in g:
    print(j)