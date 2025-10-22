def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError: # Quais são as excepções.
        print("Erro: Divisão por zero não é permitido.")
    else:
        print(f"Resultado da divisão: {resultado}")
    finally:
        print("Operação de divisão concluida.")

#exemplo de uso
#dividir(10, 2)
#dividir(10, 0)

def converter_para_inteiro(valor):
    try:
        numero = int(valor)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um numero válido.")
    else:
        print(f"Numero convertido: {numero}")
    finally:
        print("Operção de conversão concluída.")

#exemplo de uso
#converter_para_inteiro("123")
#converter_para_inteiro("abc")

def acessar_elemento(lista, indice):
    try:
        elemento = lista[indice]
    except IndexError:
        print("Erro: Indice fora do intervalo.")
    else:
        print(f"Elemento acessado: {elemento}")
    finally:
        print(f"Operação de acesso á lista concluida.")

#exemplo de uso
lista = [1, 350, 3]
acessar_elemento(lista, 1)
acessar_elemento(lista, 5)