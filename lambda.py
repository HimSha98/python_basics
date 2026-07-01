# lambda args: expression

# NORMAL FUNCTION
# def add_func(x,y) :
#     return(x + y)

# print(add_func(8,3))

# LAMBDA FUNCTIONS
# add = lambda x,y: x + y
# print(add(5,9))

# nums = [2, 5, 6, 3, 4, 7, 8]

# square_nums = list(map(function, iteration))

# USE OF MAP FUNCTION 
# square_nums = list(map(lambda x: x**2, nums))

# print(square_nums)

# USE OF FILTER FUNCTION
# even_nums = list(filter(lambda x: x % 2 == 0, nums))

# print(even_nums)

# USE OF REDUCE FUNCTION
from functools import reduce
nums = [1, 2, 3, 4,]
product = reduce(lambda x,y: x * y, nums)

print(product)