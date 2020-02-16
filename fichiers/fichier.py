
try:
    fic = open("file.txt","r")

    print(fic.read())

    line = fic.readline()
    print(line)
    
    line = fic.readline()
    print(line)
    
    line = fic.readline()
    print(line)
    
    line = fic.readlines()
    print(line)
    
    fic.close()

    if fic.closed :
        print("file closed")
    else:
        print("file not closed")
except FileNotFoundError :
    print("file not found")



with open("file.txt","r") as fic : 
    content = fic.read()
    print(content)
    #pas besoin de fermer le fichier avec with

with open("file.txt","w") as fic : 
    fic.write(str(15))
    fic.write("\nbonjour les amies\n")
    fic.write("cv\n")
