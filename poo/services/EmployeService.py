import pymysql


class EmployeService:

    def __init__(self):
        pass

    def createEmp(self,nom,sexe,age):
        try:
            cnx = pymysql.connect(host='localhost',user='root',passwd='',database='python_tutorial')
            cursor = cnx.cursor()
            mysql_insert_query = "INSERT INTO employe(id,nom,sexe,age) VALUES(Null,%s,%s,%s)"
            data = (nom,sexe,age)
            cursor.execute(mysql_insert_query,data)
            cnx.commit()
            print("create function")
        except Exception as error:
            print("failed to insert statement : {}".format(error))
        finally :
            cursor.close()
            cnx.close()
    
    def create(self,emp):
        try:
            cnx = pymysql.connect(host='localhost',user='root',passwd='',database='python_tutorial')
            cursor = cnx.cursor()
            mysql_insert_query = "INSERT INTO employe(id,nom,sexe,age) VALUES(Null,%s,%s,%s)"
            data = (emp.nom,emp.sexe,emp.age)
            cursor.execute(mysql_insert_query,data)
            cnx.commit()
            print("create function")
        except Exception as error:
            print("failed to insert statement : {}".format(error))
        finally :
            cursor.close()
            cnx.close()

    def update(self,emp):
        try:
            cnx = pymysql.connect(host='localhost',user='root',passwd='',database='python_tutorial')
            cursor = cnx.cursor()
            mysql_insert_query = "UPDATE employe SET nom=%s, sexe=%s, age=%s WHERE id=%s"
            data = (emp.nom,emp.sexe,emp.age,emp.id)
            cursor.execute(mysql_insert_query,data)
            cnx.commit()
            print("create function")
        except Exception as error:
            print("failed to insert statement : {}".format(error))
        finally :
            cursor.close()
            cnx.close()

    def findAll(self):
        try :
            cnx = pymysql.connect(host='localhost',user='root',passwd='',database='python_tutorial')
            cursor = cnx.cursor()
            mysql_select_query = "SELECT * FROM employe"
            cursor.execute(mysql_select_query)
            employes = cursor.fetchall()
            print("findAll function")
            return employes
        except Exception as error:
            print("failed to select statement : {}".format(error))
        finally :
            cursor.close()
            cnx.close()
        
    def delete(self,id):
        try:
            cnx = pymysql.connect(host='localhost',user='root',passwd='',database='python_tutorial')
            cursor = cnx.cursor()
            mysql_insert_query = "DELETE FROM employe WHERE id = %s"
            data = (id)
            cursor.execute(mysql_insert_query,data)
            cnx.commit()
            print("delete function")
        except Exception as error:
            print("failed to delete statement : {}".format(error))
        finally :
            cursor.close()
            cnx.close()

    def findById(self,id):
        try :
            cnx = pymysql.connect(host='localhost',user='root',passwd='',database='python_tutorial')
            cursor = cnx.cursor()
            mysql_select_query = "SELECT * FROM employe WHERE id = %s"
            data = (id)
            cursor.execute(mysql_select_query,data)
            employe = cursor.fetchall()
            print("findById function")
            return employe
        except Exception as error:
            print("failed to select by id statement : {}".format(error))
        finally :
            cursor.close()
            cnx.close()



