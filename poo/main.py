
from classes.Employe import Employe
from classes.Commerciale import Commercial
from classes.Comptable import Comptable
from services.EmployeService import EmployeService 

es = EmployeService()

#empl = Employe(2,'said','F',65)
#es.update(empl)

#emp = Employe(None,"samir","H",46)
#es.createEmp("safwan","H",36)
#es.create(emp)

"""
for row in es.findAll():
    print(row)

es.delete(6)

for row in es.findAll():
    print(row)
"""

#findById Function
"""
for row in es.findById(2):
    print(row)
"""




"""
emp = Employe(1,"salah","H",30)
emp.afficher()
print("*****************")

comp = Comptable(2,"said","H",26,7000)
comp.afficher()
comp.AficherComp()   
print("*****************")

com = Commercial(2,"saad","H",56,0.40)
com1 = Commercial(5,"salah","H",48,0.40)
com.afficher()
com.affiherComm()
if com.compare(com1) :
    print("the commercials have the same marge") 
print("*****************")

    """