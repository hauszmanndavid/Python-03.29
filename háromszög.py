class Háromszög:
    def Kerulet(A,B,C):
        return round(A + B + C, 4)




A = input("A oldal: ")
B = input("B oldal: ")
C = input("C oldal: ")

f = open("eredmeny.txt","r")
kerület = Kerulet(A,B,C)

print("Kerület: ", kerület)