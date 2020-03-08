#les boucle on python
import os
# While lop

etat_jeu = True

while etat_jeu :
    input_text = input("write something here : \n")
    if input_text == "again" : 
        continue
    elif input_text == "stop" : 
        break
    elif input_text == "clear" :
        os.system("cls")
    elif input_text == "test" :
        print("yes : ",input_text)
    else:
        print("write agian or stop or test")
    
print("see you ext time")
       
# for lop 
person_list = ["salah","said","saad","safaa","samir","saad"]
person_list1 = [{"name":"salah","age":45},{"name":"said","age":75},{"name":"safaa","age":55}]
"""
for p in person_list1 :
    print(p["name"] , " is " , p["age"] , "years old")
"""
for a in range(2,7): #for "variable" in range("start_number", "end_number"):
 print(a)