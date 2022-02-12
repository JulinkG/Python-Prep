from sqlite3 import enable_callback_tracebacks


# 1.- Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
number=2
if (number > 0):
    print("El número es positivo")
elif (number < 0):
    print("El número es negativo")
else: 
    print("El número es cero")

# 2.- Crear dos variables y un condicional que informe si son del mismo tipo de dato

a="variable a"
b= True
if (type(a)==type(b)):
    print("Las variables son del mismo tipo")
else:
    print("Las variables no son del mismo tipo")

# 3.- Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range(1,21):
    if (n % 2 ==0):
        print(str(n), "es par")
    else:
        print(str(n), "no es par")

# 4.- En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for a in range(0,6):
    print(a**3)

# 5.- Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

n = 6
for i in range(0, n):
    print(i)

# 6.- Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

n = 3
if (type(n) == int):
    if (n > 0):
        factorial = n
        while (n > 2):
            n = n - 1
            factorial = factorial * n
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')
    
# 7.- Crear un ciclo for dentro de un ciclo while

# 8.- Crear un ciclo while dentro de un ciclo for

# 9.- Imprimir los números primos existentes entre 0 y 30

# 10.- ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# 11.- En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# 12.- Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13.- Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# 14.-  Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# 15.-  Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

