import math

class Háromszög:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def Szerkeszhetőség(self):
        return (self.a + self.b > self.c and
                self.b + self.c > self.a and
                self.c + self.a > self.b)
    
    def Kerület(self):
        return self.a + self.b + self.c
    
    def Terület(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def Háromszögbe_írható_kör(self):
        return self.Terület() / (self.Kerület() / 2)
    
    def Beírás(self):
            f = open("eredmeny.txt", "a")
            if self.Szerkeszhetőség():
                f.write(f"Kerület: {self.Kerület()}\n")
                f.write(f"Terület: {self.Terület()}\n")
                f.write(f"Szerkeszthető: Igen\n")
                f.write(f"Háromszögbe írt kör sugara: {self.Háromszögbe_írható_kör()}\n")
            else:
                f.write("Nem lehetséges a háromszog létrehozása.\n")


a = float(input("Adja meg az a oldal hosszát: "))
b = float(input("Adja meg a b oldal hosszát: "))
c = float(input("Adja meg a c oldal hosszát: "))

háromszög = Háromszög(a, b, c)
háromszög.Beírás()

if Háromszög.Szerkeszhetőség():
    print(f"A háromszög kerülete: {Háromszög.Kerület()}")
    print(f"A háromszög területe: {Háromszög.Terület()}")
    print(f"A háromszög szerkeszthető: Igen")
    print(f"A háromszögbe írható kör sugara: {Háromszög.Háromszögbe_írható_kör()}")
else:
    print("Nem lehet létrehozni a háromszöget.")

