print("Bienvendio a la calculadora que no es calculadora ")
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
operador = input("Que operación desea realizer? +, -, /, * : ")


if operador == "+":
    operacion = numero1 + numero2
    print(operacion)

elif operador == "-":
    operacion = numero1 - numero2
    print(operacion)

elif operador == "/":
    operacion = numero1 / numero2
    print(operacion)

elif operador == "*":
    operacion = numero1 * numero2
    print(operacion)
