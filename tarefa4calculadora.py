# Calculadora Simple en Python
# Este es un programa sencillo de calculadora que permite al usuario 
# realizar operaciones matemáticas básicas: suma, resta y multiplicación.
# Funciones de la calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b): 
    return a * b 

print("Calculadora simple") 
num1 = float(input("Introduce o primero número: ")) # 
num2 = float(input("Introduce o segundo número: "))
print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2)) 
print("Multiplicación:", multiplicar(num1, num2))
