#declaramos la lista
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
#como las listas empiezan en el 0, el color que se encuentra en la posicion 3 es el amarillo, el rojo en la posicion 0 y el rosa en el 7
print(f"{colores[3]}, {colores[0]}, {colores[7]}")
numeros = ["tres", "dos", "cinco", "cuatro", "uno"]
#nueva lista
colores_ = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#ppdemos acceder a los ultimos elementos de las listas usando numeros negativos. Con -1 accedemos al ultimo elemento de la lista, -2 al penultimo elemento y asi
#sucesibamente 
print(f"{colores_[-1]}, {colores_[5]}, {colores_[-2]}, {colores_[-7]}, {colores_[-10]}")
#eliminamos elementos con del
del colores_[1]; del colores_[3]; del colores_[-4]; del colores_[-3]
print(colores_)
#con .remove() eleminamos un elemento por nombre
colores_.remove('amarillo'); colores_.remove("rojo")
print(colores_)
#el metodo .pop() funciona igual que del pero .pop() nos permite almacenar el valor del elemento eliminado
color1 = colores_.pop(0); color2 = colores_.pop(-2)
print(f"{colores_}, {color1}, {color2}")

#el metodo .append() nos permite agregar elementos a una lista y el elemento nuevo quedara en la ultima posicion de la lista
colores_.append('fuxia'); colores_.append("celeste")
print(colores_)
#con el metodo .insert() podemos insertar un nuevo elemento a una lista con una posicion especifica
colores_ = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores_.insert(6, "magenta"); colores_.insert(-1, "turquesa")
print(colores_)

#con el metodo .sort() podemos ordenar listas desde la a-z, pero los cambios hechos con este metodo son permamentes en la lista
#si no queremos hacer cambios permamentes en la lista debemos usar sorted()
#si queremos un ordenamiento de z-a debemos poner .sort(reverse=True)
#si queremos saber el largo de una lista debemos usar el metodo len() y este dato lo podemos guardar en una variable
#lenght = len(colores_)
colores_ = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores_.sort(reverse=True)
print(colores_)
