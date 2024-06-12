### Operadores Aritmeticos Python ####

print(3 + 4)#Suma
print(3 - 4)#resta
print(3 * 4)#Multiplicación
print(3 / 4)#División
print(10 % 2)#Perador de modulo, Regresa el residuo de una división.
print(10 % 9)
print(10 // 3)#división flor-división va llegar a un aproximado entero
print(2 ** 3)#dos elevado al 3 (Potencias)


print("Hola" + "Python")#Concatena textos
# print("Hola" + 5) #No obstante no es posible sumar valores distintos
print("Hola " + str(5))#Forzar string o colocar "5"

print("Adios " * 5)#Curiosamente si funciona string con operador multi


### Operadores Comparativos ###

print(3 > 4)#Mayor que
print(3 < 4)#Menor que
print(3 >= 4)#Mayor o igual que
print(3 <= 4)#Menor o igual que
print(3 == 4)#Igual
print(3 != 4)#Distinto

#En textos con los menor y mayor que. Este hace ordenación Alfabetica
print("hola" > "python")
print("aaa" < "bbb")
print("bbb" > "ccc")

#siki asu oidrua ser distinto por su tamñano de cadena de texto
print(len("aaa") <= len("abaa"))


### Operadores Logicos ###

print(3 > 4 and "hola" > "python")
print(3 > 4 or "hola" > "python")
print(not(3 > 4))
print(not(10 > 2 and 8 > 2))
print(10 > 2 or 8 < 2)
