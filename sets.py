"""
A set object is an unordered collection of distinct hashable objects. It is commonly used in membership testing,
removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference,
and symmetric difference.

Sets support x in the set, len(set), and for x in set like other collections. 
Set is an unordered collection and does not record element position or order of insertion. 
Sets do not support indexing, slicing, or other sequence-like behavior.

There are currently two built-in set types, set, and frozenset. 
The set type is mutable - the contents can be changed using methods like add() and remove(). 
Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. 
The frozenset type is immutable and hashable - its contents cannot be altered after it is created; it can, 
therefore, be used as a dictionary key or as an element of another set.
"""

#A new empty set
setx = set()
print(setx)
#A non empty set
n = set([0, 1, 2, 3, 4, 5])
print(n)

"""Add member(s) in Python set:"""
#A new empty set
color_set = set()
#Add a single member
color_set.add("Red")
print(color_set)
#Add multiple items
color_set.update(["Blue", "Green"])
print(color_set)

"""Remove item(s) from Python set:
pop(), remove() and discard() functions are used to remove individual item from a Python set. 
See the following examples :"""

#pop() function:
num_set = set([0, 1, 2, 3, 4, 5])
num_set.pop()
print(num_set)
num_set.pop()
print(num_set)

#remove() function:
num_set = set([0, 1, 2, 3, 4, 5])
num_set.remove(0)
print(num_set)

#discard() function:
num_set = set([0, 1, 2, 3, 4, 5])
num_set.discard(3)
print(num_set)

#Union
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
seta = setx | sety
print (seta)

