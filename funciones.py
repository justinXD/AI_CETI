def suma(n1,n2):#declaramos la funcion con dos parametros que le llegan:n1 y n2
    total =n1+n2#hacemos la suma de los parametro
    print("El resultado es: ",total)#mostramos el resultado de la suma

suma(15,15)#mandamos en el primer caso 15 y 15 para que sea 30
suma(25,25)#en este 25 y 25 para que sea 50
suma(28500,28500)#y aqui para que sea 57000

#funcion con diferente cantidad de argumentos

def colores(*args):#definimos la funcion con args para que pueda variar de acuerdo a lo que vayamos pidiendo
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')#imprimimos los valores que se mandaron

colores('rojo', 'azul', 'verde', 'amarillo')#mandamos los diferentes valores
colores('lila', 'negro', 'rojo')#solo apareceran los valores que esten en la posicion 1 y 0
colores('rosa','negro')
colores('marrón', 'naranja')