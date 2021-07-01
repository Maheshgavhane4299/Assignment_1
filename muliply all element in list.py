# using math module
from math import *

list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = prod(list1)
result2 = prod(list2)
print(result1)
print(result2)



#using reduce and lambda function
from functools import reduce

list1 = [2,4,6,8,10]
list2 = [9,8,7,6,5]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)