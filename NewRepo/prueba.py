
def funcion():
    suma=1
    a=0
    b=a+suma
    print(b)
#--------------------------------------------------------------
def f(x):
    return x*x

g=int(input("dato: "))
print(f(g))
funcion()
#--------------------------------------------------------------
def h(z):
    return z*z

print(h(2))
#--------------------------------------------------------------
def factorial():
    s=10*9*8*7*6*5*4*3*2*1
    print(s)

factorial()
#--------------------------------------------------------------
def d(q):
    return q**2

print(d(10))

#--------------------------------------------------------------
import math #libreria de numeros irracionales y demas elementos matematicos
def area(r):
    area=math.pi*r**2
    return area

def perimetro(r):
    peri=2*math.pi*r
    return peri

def volumen(r):
    vol=(4/3)*math.pi*r**3
    return vol


t=float(input("Ingrese el radio: "))
print("El área del circulo es: ",area(t))
print("El perímetro del circulo es: ",perimetro(t))
print("El vólumnen del circulo es: ",volumen(t))

#--------------------------------------------------------------

v=(5//2)*2
print(v)

#--------------------------------------------------------------

def rectangulo(b,a):
    p=b*a
    return p


print("el area es :",rectangulo(2,3))