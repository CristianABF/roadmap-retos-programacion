'''
Funciones definidas por el usuario
'''

# Simples

def greet():
    print("Hola, Python!")

greet()

# Con retorno

def return_greet():
    return "Hola, Python!"

greet = return_greet()
print(greet)

# Con un argumento

def arg_greet(name):
    print("Hola, {name}!")

arg_greet("Cris")

# Con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Cris")
args_greet(name="Cris", greet="Hi")

#Con un argumento predeterminado

def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet()
default_arg_greet("Cris")

# Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("hi", "cris"))

# Funcion con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Cris", "Mouredev", "Comunidad")

# Con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Cris",
    alias="CristianABF",
    age=22
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python!")
    inner_function()

outer_function()

"""
Funciones del lenguaje(built-in)
"""
print(len("CristianABF"))
print(type("CristianABF"))
print("CristianABF").upper())

"""
Variables locales y globales
"""

global_var = "Python"

print(global_var)

def hello_python():
    loval_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(globar_var)
print(local_var) # No se puede acceder desde fuera de la funcion

"""
Extra
"""

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count


print(print_numbers("Fizz", "Buzz"))
