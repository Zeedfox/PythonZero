#Variables adecuados
first_variable = "My first string Variable"
print(first_variable)

my_int_Variable = 5
print(my_int_Variable)

my_bool_variable = True
print(my_bool_variable)

#se puede concatenar facilmente con solo el uso de ,
print(first_variable, my_int_Variable, my_bool_variable)


#str sirve para convertir a String...
int_to_str_variable = str(my_int_Variable)
print(int_to_str_variable)
print(type(int_to_str_variable))#recordar que type() sirve para ver el tipo dato


print(type(print("Mi cadena texto"))) #tipo "Nonetype", por que es una funcion


#Funcion len
print(len(first_variable)) #Regresa el tamaño de la variable


#Variables en una sola linea. (No tan recomendado, pero posible...9)
nombre, apellido, alias, edad = "Zeed", "Fox", "Daxter", 25
print("Me llamo: ", nombre, apellido, ". Mi edad es:", edad, ". y mi alias, ", alias)


#input sirve para capturar desde la consola datos... por defecto los toma como string
dato_usuario = input("Ingrese un dato! El que sea es valido:  ")
print('Usted ingreso: ', dato_usuario, 'El cual se trata de un..', type(dato_usuario))


#En python se pueden cambiar los tipos de datos!!!!
dato_usuario = 35.7
print(dato_usuario, " y ahora es un ", type(dato_usuario))


#¿Forzamos el tipo de variable?
address: int = '49.78' #Parece que no ayuda, posiblemente en solo inputs
print(address, " es.. ",type(address))
address: int = input("ingrese un numero") #Parece no afectar...
print(address, " es.. ",type(address))
#En definitivamente no podemos forzarlo... (al menos no de este modo..)



#aqui si que se "convierte"
address = int(5.98)
print(address, " es.. ",type(address))
address = float(8)
print(address, " es.. ",type(address))

# Algunos tipos de variables basicos
print(type("Solo un dato")) #Tipo 'str'
print(type(5)) #Tipo 'int'
print(type(1.5)) #Tipo 'float'
print(type(3 + 1j)) #Tipo 'complex'
print(type(true)) #Tipo 'bool'

