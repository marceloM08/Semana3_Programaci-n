#sumar dos numeros y mostrar el resultado
#Parametro es la variable que se define cuando se crea la funcion
def getSum(numb1, numb2):
    return numb1 + numb2

def showResult(message, result):
    return f"{message} {result}"

print("Dime un numero: ")
num1 = float(input())
print("Dime otro numero: ")
num2 = float(input())
#argumento es el valor que se envia a la funcion cuando se llama
sum = getSum(num1, num2)
print(showResult("La suma es: ", sum))