x = 0#declaramos las variable
y = 0
z = 10
while x!=15:#la primera se ejecutara siempre y cuando sea diferente de 15, aumenta de 5 en 5, y hasta que llega a 15 se rompe el ciclo
    x=x+5
    print(x)

while y !=-100:#aqui la condicion es distinta, se inicializa en 0, y al llegar a -100 se rompe el ciclo, se disminuye de 20 en 20
    y = y-20
    print(y)

while z != 0:#aqui se inicializa en 10, y al disminuirse de 1 en 1 hasta llegar al 0 se rompe el ciclo
    z=z-1
    print("El valor del bucle es: ",z)

#bucle con condiciones
x = 0#declaramos las variables
while x <= 30:#se inicia el while, y se rompe cuando x sea mayor que 30
    x = x+1
    if x == 4 or x == 6 or x == 10:#ejecutamos la primer condicion, si es igual a 4, 6, o 10, imprime y se salta al siguiente ciclo
        print("Se salto el valor: ", x)
        continue
    
    print("El valor del bucle es: ", x)#cuando sea igual a 15, se va a romper el bucle
    if x == 15:
        break

if x == 15:#cuando se rompa el bucle, se imprime ya fuera del ciclo while lo siguiente
        print('se rompió la ejecución del bucle cuando x valía ', x)

#bicle for
colores = ('rojo','azul','verde','amarillo')#definimos la lista
for x in colores:#y en for usamos la variable x, que ira tomando cada posicion de la lista, para luego imprimirla
    print('El color es: ' + x + '.')


for x in range(7,700,100):#usamos range para definir sus parametros, inicianizandolo en 7,hasta llegar al 100, con saltos de 100
    print(x)