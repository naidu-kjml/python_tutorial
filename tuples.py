"""
A tuple is a container which holds a series of comma-separated values (items or elements) between parenthesessuch as an (x, y) co-ordinate.
Tuples are like lists, except they are immutable (i.e. you cannot change its content once created) and can hold mix data types.
Tuples play a sort of "struct" role in Python -- a convenient way to pass around a little logical,fixed size bundle of values.
"""

#create an empty tuple
tuplex = tuple()
print (tuplex)

#create a tuple with different data types
tuplex = ('tuple', False, 3.2, 1)
print (tuplex)

#create a tuple with numbers, notation without parenthesis
tuplex = 4, 7, 3, 8, 1 
print (tuplex)

#create a tuple of one item, notation without parenthesis
tuplex = 4, 
print (tuplex)

#create a tuple from a iterable object
tuplex = tuple([True, False]) 
print (tuplex)

"""How to get an item of the tuple in Python?"""

#create a tuple
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e") 
print(tuplex)

#get item (4th element)of the tuple by index
item = tuplex[3]
print(item)

#get item (4th element from last)by index negative
item1 = tuplex[-4]
print(item1)

"""How to know if an element exists within a tuple in Python?"""
print("r" in tuplex)
print(5 in tuplex)

"""List To Tuple"""
#create list
listx = [5, 10, 7, 4, 15, 3]
print(listx)
#use the tuple() function built-in Python, passing as parameter the list
tuplex = tuple(listx)
print(tuplex)

"""Add item in Python tuple!"""

#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)
