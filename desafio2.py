def fibonacci(numero):
    num1 = 0
    num2 = 1
    cont = 3
    if numero == 0 or numero == 1:
        return 'Este numuro pertence a sequência de fibonacci'
    while cont <= numero:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        cont += 1
        if numero == num3:
            return 'Este numero pertence a sequência de fibonacci'
    return 'Este numero não pertene a sequência de fibonacci'
numero = int(input('Digite um numero:'))
print(fibonacci(numero))
