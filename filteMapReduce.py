
nums = [3,6,4,5,8,2,9,6]
print(nums)

"""
 now we will do some filtring, we will print only the number with  %/2 = 0, 
 we're going to use filter function that accept two parametres(function , list)
 we must convert it to list because we traying to return a list
"""
def is_even(n) :
    return n % 2 == 0
#evens = list(filter(is_even,nums))
evens = list(filter(lambda n: n % 2 == 0,nums))
print(evens)

"""
now we will do some operation in filtring data with map function,we will double the values by 2 n*2
map function that accept two parametres(function , list)
 we must convert it to list because we traying to return a list
"""
def is_double(n):
    return n * 2

#doubles = list(map(is_double,evens))
doubles = list(map(lambda n: n * 2, evens))
print(doubles)

"""
now we will do sum operation using reduce function
"""
from functools import reduce

def is_sum(a,b):
    return a + b

#sum = reduce(is_sum,doubles)
sum = reduce(lambda a,b: a + b ,doubles)
print(sum)


