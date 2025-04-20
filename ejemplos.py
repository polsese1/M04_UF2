#!/usr/bin/python3

version = 0.5

app_title = "Playlist v"+str(version)

print(app_title)

print("-"*len(app_title))


def saluda ():
	print("Hola!")


def suma (num1, num2):
	return num1+num2


def despide (quien="Jacinto"):
	print("Estás despedido", quien)


def retorna_multiple ():
	uno = 1
	dos = 3

	return uno, dos


if False:
	print("Cierto")
else:
	print("Falso")

primero = 5
segundo = 3

if primero > segundo:
	print("El primero es mayor que el segundo")
elif primero < segundo:
	print("El segundo es mayor que el primero")
else:
	print("son iguales")

contador = 10

while contador > 0:
# print(contador)
	contador -= 1

print("-----")

for num in range(1, 10): # range(INICIAL, FIN, PASOS
	print(num)


personas = ["jaimito", "Jacinto", 33, "Anselmito"]

print(personas[2])

print(">", dato)

personaje = {
	"nombre": "Paquito",
	"edad": 33, 
	"pelo": "marrón"
}


#print("Personaje:", personaje["nombre"])

for clave in personaje:
	print(">>", clave, personaje[clave])

for clave, valor in personaje.items():
	print(">>>", clave, valor)

saluda()

resultado = suma(3, 5)

print(resultado)

despide()
despide("Ramiro")


valor1, valor2 = retorna_múltiple()


print("Valores:", valor1, valor2)


nombre = input("¿Cómo te llamas?")

print(nombre)
