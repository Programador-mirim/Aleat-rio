a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida!!!!!!!!!!!!!")
    return a / b

print(f"A soma é: {soma(a, b)}")
print(f"A subtração é: {subtracao(a, b)}")
print(f"A multiplicação é: {multiplicacao(a, b)}")
print(f"A divisão é: {divisao(a, b)}")