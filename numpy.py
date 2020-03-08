from array import *


arr2 =  array("i",[1,5,68,3,5])

print(arr2)
print(arr2.buffer_info())#the firsy parametre is the adresse and the second is the size

arr = [5,9,3,1,5]

for i in range(5):
    print(arr[i])

for i in range(len(arr)):# in case we dont know the size of the array or the list 
    print(arr[i])

for n in arr:
    print(n)

