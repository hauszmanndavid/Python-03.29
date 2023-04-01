class Háromszög:
    def Kerület(a,b,c):
         return round(a + b + c, 4)


a = float(input("A oldal: "))
b = float(input("B oldal: "))
c = float(input("C oldal: "))


kerület= Kerület(a,b,c)


print("Perimeter:", kerület)

