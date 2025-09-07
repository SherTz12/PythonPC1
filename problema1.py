# Problema 1:
# Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
# usuario haya introducido

nombre = input("Ingrese su nombre de usuario: ")

print(f"¡Hola {nombre}!")



# Problema 2:
# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
# restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
# porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
# dejar como propina.

consumo = float(input("¿De cuánto fue su consumo ($)?: "))

propina_porcentaje = float(input("¿Qué porcentaje de propina desea dejar?: "))

propina = consumo * (propina_porcentaje/100)

print(f"Debe dejar {propina:.2f}$ de propina")



# Problema 3:
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
# por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
# peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y 
# cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el 
# último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muñecas = 75

num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidos: "))

peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñecas)

print(f"El peso total del paquete es {peso_total}g")



# Problema 4:
# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
# pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
# puede ser calculada de la siguiente forma: 1+2+3+... + n = (n(n+1))/2

N = int(input("Ingrese un número entero positivo: "))

suma = N * (N + 1) // 2

print(f"La suma de los primeros {N} enteros positivos es {suma}.")



# Problema 5:
# Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
# último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
# verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

shows = int(input("¿Cuántos shows musicales has visto este último años?: "))

más_de_tres = bool(shows > 3)

print(más_de_tres)



# Problema 6:
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
# calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
# preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
# años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
else:
    precio = 10

print(f"El precio de la entrada es: ${precio}.")



# Problema 7:
# Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
# - Mostrar una suma de los dos números
# - Mostrar una resta de los dos números (el primero menos el segundo)
# - Mostrar una multiplicación de los dos números
# - En caso de introducir una opción inválida, el programa informará de que no es correcta.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

Menú = ("Elija una opción:\n1. Sumar\n2. Restar\n3. Multiplicar\nIngrese el número de la opción: ")

Opción = int(input(Menú))

if Opción == 1:
    print(f"La suma es: {num1 + num2}")
elif Opción == 2:
    print(f"La resta es: {num1 - num2}")
elif Opción == 3:
    print(f"La multuplicación es: {num1 * num2}")
else:
    print("Opción inválida")



# Problema 8:
# Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
# entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
# Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la hora del almuerzo o la hora de la cena. 
# Si no es hora de comer, no envíes nada.
# Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y suponga que el rango de tiempo de cada comida es inclusivo. 
# Por ejemplo, ya sean las 7:00, las 7:01, las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.

tiempo = input("Ingrese la hora en formato HH:MM (24h): ")

horas, minutos = tiempo.split(":")

horas = int(horas)
minutos = int(minutos)

hora_decimal = horas + (minutos / 60)

if  7 <= hora_decimal <= 8:
    print("Es hora del desayuno :)")
elif 12 <= hora_decimal <= 13:
    print("Es hora de almozar :3")
elif 16 <= hora_decimal <= 19:
    print("Es hora de cenar :o")
else:
    print("")



# Problema 9:
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience 
# leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa
# debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

cantidad = float(input("Ingrese la cantidad de dinero depositado: "))

tasa_de_interés = 4

saldo_1_año = cantidad * (1 + tasa_de_interés/100) ** 1
saldo_2_año = cantidad * (1 + tasa_de_interés/100) ** 2
saldo_3_año = cantidad * (1 + tasa_de_interés/100) ** 3

print(f"La cantidad de ahorro del primer año es: {saldo_1_año:.2f}\nLa cantidad de ahorro del segunda año es: {saldo_2_año:.2f}\nLa cantidad de ahorro del segundo año es: {saldo_3_año:.2f}")



# Problema 10:
#Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.
# Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución.
# Su programa debe indicar:
# ● En caso la ecuación cuadrática tenga solución real, su programa debe brindar la solución
# ● En caso su ecuación no tenga solución real, su programa debe brindar un mensaje que diga "Ecuación no presenta solución real"

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

if a == 0:
    print("a debe ser distinto de 0")
else:
    D = b**2 - 4 * a * c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print("Dos soluciones distintas: ")
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif D == 0:
        x = -b / (2*a)
        print("Una solución real doble: ")
        print("x = ", x)
    else:
        print("Ecuación no presenta solución real")