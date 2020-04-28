
# outer Class
class Student:

    def __init__(self,_id,_nom):
        self.id = _id
        self.nom = _nom
        self.lap = self.Laptop()
    
    # inner Class
    class Laptop :

        def __init__(self):
            self.brand = "HP"
            self.ref = "Er5fdds"
    

s1 = Student(4,"salah")
lap = s1.lap.brand
print(lap)