"""
num = int(input("Ingrese nro: "))
if num > 0 :
    print(f"el nro {num} es mayor que 0")
elif num < 0 :
    print(f"El nro {num} es menor que 0")
else :
    print(f"el nro {num} es 0")
    """



#nombre = "harry"
#print(nombre[0])
#nombres =[ "harry", "hermione", "ron"]
#for i in range(3):
#    print(nombres[i])
#print(len(nombres))
#for i in range(len(nombres)):
#     print(nombres[i])
#for unNombre in nombres:
#    print(unNombre)
#for i in [0,1,2,3,4,5]:

#    print(i)
#for i in range(6):
#    print(i)

#cantVeces=10
#for i in range(cantVeces):
#   print(i)
#def cuadrado(numero):
#    resultado= numero* numero
#    return resultado
#for i in range(10):
#     print(f"el cuadrado de {i}={cuadrado(i)}")
#class Punto():
#    def __init__(self,num1,num2):
#        self.numero1=num1
#        self.numero2=num2
#p=Punto(2,4)
#print(p.numero1)
#print(p.numero2)
"""
class Vuelo():
    def __init__(self,capacidad,nroDeVuelo):
        self.capacidad=capacidad
        self.nroDeVuelo=nroDeVuelo
        self.pasajeros=[]
    
    def agregar_pasajeros(self, nombre):
        
        if not self.asientos_disponibles():
            return False
        self.pasajeros.append(nombre)
        return True

    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)
"""
"""vuelo147=Vuelo(3,147)
#print(vuelo147.capacidad)
#print(vuelo147.nroDeVuelo)
vuelo147.agregar_pasajeros("juan carlos")
vuelo147.agregar_pasajeros("pepe pompin")
print(vuelo147.pasajeros)
vuelo147.agregar_pasajeros("pepa pompotas")
print(vuelo147.asientos_disponibles())
print(vuelo147.pasajeros)
vuelo147.agregar_pasajeros("pepina nina")
print(vuelo147.asientos_disponibles())
print(vuelo147.pasajeros)"""

"""vuelo147=Vuelo(2,147)
personas=["harry","hermione","ron"]
for una_persona in personas:
    if vuelo147.agregar_pasajeros(una_persona):
        print(f"se agrego a {una_persona} al vuelo nro {vuelo147.nroDeVuelo}")
    else:
        print(f"no se pudo agregar a {una_persona} por limite de la capacidad de vuelo")"""
"""
class Empleado():
     num_empleado=0
     porcentaje_aumento=1.04
     def __init__(self, nombre, apellido, sueldo):
        self.nombre=nombre
        self.apellido=apellido
        self.sueldo=sueldo
        self.email = nombre + '.' +apellido+'@miempresa.com'
        Empleado.num_empleado += 1

     def nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)

     def aplicar_aumento(self):
         self.sueldo=int(self.sueldo*porcentaje_aumento)

class Desarrollador(Empleado):
   porcentaje_aumento=1.1
   def __init__(self, nombre, apellido,sueldo,lenguaje):
       super().__init__(nombre,apellido,sueldo)
       self.lenguaje=lenguaje

empleado1=Desarrollador("Harry","Potter",999,"Python")


print(empleado1.email)
print(empleado1.num_empleado)
print(empleado1.porcentaje_aumento)
print(empleado1.sueldo)
empleado2=Empleado("Ron","Weasley",999)
print(empleado2.email)
print(empleado2.num_empleado)
print(empleado2.porcentaje_aumento)
print(empleado2.sueldo)
print(empleado1.lenguaje)"""

"""
class Tomate():
    def tipo(self):
        print("vegetal")
    def color(self):
        print("rojo")

class Manzana():
    def tipo(self):
        print("fruta")
    def color(self):
        print("rojo")

def func(obj):
            obj.tipo()
            obj.color()

unTomate=Tomate()
unaManzana=Manzana()
func(unTomate)
func(unaManzana)"""

"""
class Argentina():
    def capital(self):
        print("CABA")
    def idioma(self):
        print("espaniol")

class EEUU():
    def capital(self):
        print("washington")
    def idioma(self):
        print("ingles")

paisArgentina = Argentina()
paisEEUU = EEUU()

for unPais in (paisArgentina, paisEEUU):
    unPais.capital()
    unPais.idioma()

"""
"""
class Ave():
    def introduccion(self):
        print("existen muchos tipos de aves")
    def vuelo(self):
        print("algunas aver pueden volar y otras no")

class perico(Ave):
    def vuelo(self):
        print("pueden volar")

class pinguino(Ave):
    def vuelo(self):
        print("los pinguinos no pueden volar")

unAve=Ave()
unPerico=perico()
unPinguino= pinguino()

unAve.introduccion()
unAve.vuelo()

unPerico.introduccion()
unPerico.vuelo()

unPinguino.introduccion()
unPinguino.vuelo()
"""


"""
def mi_mensaje(f):
    def wrapper():
        print("esta funcion esta por comenzar")
        f()
        print("mi funcion ha terminado")
    return wrapper

@mi_mensaje
def hola():
    for miNumero in range(3):
        print(miNumero)
hola()

"""
"""
def cuadrado(x):
    return x*x

print(cuadrado(5))

cuadrado=lambda x: x*x
print(cuadrado(5))
"""

"""
personas=[
    {"nombre":"Harry","casa":"griffindor"},
    {"nombre":"Cho","casa":"ravenclaw"},
    {"nombre":"Draco","casa":"slytherin"}
]

#def f(unaPersona):
#    return unaPersona["nombre"]

#personas.sort(key=f)
#print(personas)


personas.sort(key=lambda unaPersona: unaPersona["nombre"])
print(personas)
personas.sort(key=lambda unaPersona: unaPersona["casa"])
print(personas)
"""

"""
import sys

try:
    numero1=int(input("ingrese numero 1: "))
    numero2=int(input("ingrese numero 2: "))
except ValueError:
    print("error. no valido")
    sys.exit(1)

try:
    resultado=numero1/numero2
except ZeroDivisionError:
    print("error, no se puede dividir por cero.")
    sys.exit(1)

print(f"el resultado de la operacion es {numero1}/{numero2}={resultado}")
"""