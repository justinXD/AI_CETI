num1 = 15
num2 = 20

if num1 < num2:
	print('Se ejecuta el if.')

num1 = 1450
num2 = 60

if num1 > num2:
	print('Se ejecuta el if.')

num1 = 60
num2 = 60

#esta condicional no se va a cumplir porque los dos numeros son iguales

if num1 != num2:
	print('Se ejecuta el if.')

#corrigiendo el codigo
#color = rojo

#else color == rojo
#Print "El color es rojo."
#if color != rojo
#Print "El color no es rojo."

#definimos color como string
color = "amarillo"
if color == "rojo":
    print("el color es rojo")
else:
    print("el color no es rojo")
	
#condicionales multiples
edad = int(input('¿Cuál es tu edad?\n'))#pide la edad
if edad <= 0:#si la edad es menor o igual que 0 se ejecuta lo siguiente
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:#si esta entre 1 y 18 años, ejecuta el elif e imprime que es menor de edad
	print('Eres menor de edad.')
elif edad < 100:#si es menor que 100 años, pero mayor de 18, ejecuta lo siguiente
	print('Eres mayor de edad.')
elif edad >=18 and edad <=45:#si tiene entre 18 y 45, imprime que tiene entre 18 y 45 xD
    print("tienes entre 18 y 45")
elif edad >100 and edad <=120:#y si tiene entre 100 y 120, imprime que pocos viven hasta esa edad
    print("pocos viven hasta esta edad")
else:
	print('Edad no válida.')#de ser ninguno el caso, ya sea un numero negativo o mayor a 120, ejecuta lo siguiente

#verificar contenido dentro de una tupla
entrada = input('Introduce el color:\n')#pedimos el color a buscar
tupla = ("rojo","azul","verde","negro")#declaramos la tupla
if entrada in tupla:#si el color buscado esta dentro, corre la tupla
    print('El color que buscas está en la lista.')
else:#de ser lo contrario, se corre el else
    print('El color que buscas no está en la lista.')