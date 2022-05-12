import random

ca1 = random.uniform(1,100).__round__(2)
ca2 = random.uniform(1,100).__round__(2)
ca3 = random.uniform(1,100).__round__(2)
ca4 = random.uniform(1,100).__round__(2)
ca5 = random.uniform(1,100).__round__(2)
ca6 = random.uniform(1,100).__round__(2)
ca7 = random.uniform(1,100).__round__(2)
ca8 = random.uniform(1,100).__round__(2)
ca9 = random.uniform(1,100).__round__(2)
ca10 = random.uniform(1,100).__round__(2)
ca11 = random.uniform(1,100).__round__(2)
ca12 = random.uniform(1,100).__round__(2)
ca13 = random.uniform(1,100).__round__(2)
ca14 = random.uniform(1,100).__round__(2)
ca15 = random.uniform(1,100).__round__(2)
ca16 = random.uniform(1,100).__round__(2)
ca17 = random.uniform(1,100).__round__(2)
ca18 = random.uniform(1,100).__round__(2)
ca19 = random.uniform(1,100).__round__(2)
ca20 = random.uniform(1,100).__round__(2)
ca21 = random.uniform(1,100).__round__(2)
ca22 = random.uniform(1,100).__round__(2)
ca23 = random.uniform(1,100).__round__(2)
ca24 = random.uniform(1,100).__round__(2)
ca25 = random.uniform(1,100).__round__(2)

print("\t\n velocidades de los caballos")
print(f"\t\n caballo 1 {ca1} \t\n caballo 2 {ca2} \t\n caballo 3 {ca3} \t\n caballo 4 {ca4} \t\n caballo 5 {ca5} \t\n caballo 6 {ca6} \t\n caballo 7 {ca7} \t\n caballo 8 {ca8} \t\n caballo 9 {ca9} \t\n caballo 10 {ca10}")
print(f"\t\n caballo 11 {ca11} \t\n caballo 12 {ca12} \t\n caballo 13 {ca13} \t\n caballo 14 {ca14} \t\n caballo 15 {ca15} \t\n caballo 16 {ca16} \t\n caballo 17 {ca17} \t\n caballo 18 {ca18} \t\n caballo 19 {ca19} \t\n caballo 20 {ca20}")
print(f"\t\n caballo 21 {ca21} \t\n caballo 22 {ca22} \t\n caballo 23 {ca23} \t\n caballo 4 {ca24} \t\n caballo 25 {ca25}")

grupo1 = [ca1, ca2, ca3, ca4, ca5]
grupo2 = [ca6, ca7, ca8, ca9, ca10]
grupo3 = [ca11, ca12, ca13, ca14, ca15]
grupo4 = [ca16, ca17, ca18, ca19, ca20]
grupo5 = [ca21, ca22, ca23, ca24, ca25]

grupo1.sort()
grupo2.sort()
grupo3.sort()
grupo4.sort()
grupo5.sort()

print(f"\t\n {grupo1} \t\n {grupo2} \t\n {grupo3} \t\n {grupo4} \t\n {grupo5}")

print("\t\n Los primeros 5 ganadores tuvieron los siguientes tiempos")
print(f"\t\n {grupo1[0]} \t\n {grupo2[0]} \t\n {grupo3[0]} \t\n {grupo4[0]} \t\n {grupo5[0]}")

# grupo1[0] = random.uniform(1,100).__round__(2)
# grupo2[0] = random.uniform(1,100).__round__(2)
# grupo3[0] = random.uniform(1,100).__round__(2)
# grupo4[0] = random.uniform(1,100).__round__(2)
# grupo5[0] = random.uniform(1,100).__round__(2)
grupo6 = [grupo1[0], grupo2[0], grupo3[0], grupo4[0], grupo5[0]]
grupo6.sort()

print(f"\t\nlos primeros 5 lugares volvieron a competir y el ganador tiene un tiempo de: {grupo6[0]} y este es el caballo mas rapido")

print("\t\n Haremos una ultima carrera con el segundo y tercer lugar de la sexta carrera y los segundos lugares de la primera, segunda y tercera carrera")
# grupo6[1] = random.uniform(1,100).__round__(2)
# grupo6[2] = random.uniform(1,100).__round__(2)
# grupo1[1] = random.uniform(1,100).__round__(2)
# grupo2[1] = random.uniform(1,100).__round__(2)
# grupo3[1] = random.uniform(1,100).__round__(2)
grupo7 = [grupo6[1], grupo6[2], grupo1[1], grupo2[1], grupo3[1]]
grupo7.sort()
grupo8 = [grupo6[0], grupo7[0]]
grupo8.sort()

print("despues de 7 carreras tenemos a los dos caballos mas rapidos")
print(f"\t\nprimer lugar {grupo8[0]} \t\nsegundo lugar {grupo8[1]}")
