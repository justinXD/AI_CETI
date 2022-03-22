#las tuplas son parecidas a las listas, con la diferencia en que las tuplas no son modificables una vez ejecutado el codigo. son como listas constantes
#lista = ['rojo', 'azul', 'verde', 'amarillo']
#tupla = ('rojo', 'azul', 'verde', 'amarillo')
#las tuplas funcionan igual que las listas y tambien pueden tener diferentes tipos de datos
#declaro mi tupla
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores)
print(colores[1])
numeros = (10, 1, 5, 11)
operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1]
print(operacion)

#podemos convertir listas a tuplas y viceversa
#de lista a tupla
#lista = ['rojo', 'azul', 'verde', 'amarillo']
#tupla = tuple(lista)
#print(tupla)

#de tupla a lista
#tupla = ('rojo', 'azul', 'verde', 'amarillo')
#lista = list(tupla)
# para saber el tipo de dato debemos usar el metodo type()

colores_ = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
tupla = tuple(colores_)
print(tupla)
print(type(tupla))
