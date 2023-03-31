class Háromszög:
    def szerkeszthetőség(o):
        if ((A+B>C) and (A+C>B) and (B+C>A)):
            return "Szerkeszthető "+str(kerulet(A+B+C))
        else:
            return "Nem szerkeszthető"
    
    def kerulet(A,B,C):
        return A+B+C


f = open("eredmeny.txt","r")

A = input("A oldal: ")
B = input("B oldal: ")
C = input("C oldal: ")

print(szerkeszthetőség(o))

