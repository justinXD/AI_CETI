#primero declaramos las partes de nuestro diccionario
teclado1 ={#declaramos el diccionario
    "Categoria": "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
}

for x,y in teclado1.items():#aqui definimos X y Y, X va a momstrar las definiciones, el lado "Izquierdo", y Y va a mostrar sus atributos, y usando la funcion items, obtenemos los valores del diccionario
    print(x," = ",y,".")#imprimimos

teclado2 = {#inicializamos el diccionario, con "categoria","modelo" y "precio", con su respectivo valor
    "Categoria": "Teclados",
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }

consulta = teclado2["Modelo"]#obtenemos el valor en la posicion Modelo
consulta2 =teclado2["Precio"]#obtenemos el valor en la posicion Precio
print("El modelo",consulta,"cuesta",consulta2)#luego imprimimos y concatenamos

#ahora eliminamos alugas partes del teclado2 y eliminamos el teclado1
del teclado1#eliminamos todo el diccionario 1
del teclado2["Categoria"]#eliminamos unicamente Categoria
del teclado2["Precio"]#eliminamos unicamente Precio
print(teclado2["Modelo"])#mostramos la seccion modelo de teclado2
