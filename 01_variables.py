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