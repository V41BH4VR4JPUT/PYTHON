# map , filter and reduce functions

#map

nums = [1 , 3 , 4 , 6 , 8 ]
sq = map(lambda x : x*x , nums)
print(list(sq))

#filter
evens = filter(lambda x : x%2 == 0 , nums)
print(list(evens))

#reduce
from functools import reduce
sum = reduce(lambda x , y : x + y , nums)
print(sum)