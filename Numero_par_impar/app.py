print("==============================================")
print("Digite um numero e veja se ele é impar ou Par")
print("==============================================")
numero = int(input("Digite o numero: "))
print("-----------------------------------------------")

def Verificacao_numero_impar_par():
    verificar = int(numero % 2)
    if( verificar == 0):
        print(f"O Numero {numero} é Par")
        print("==============================================")
    else:
        print(f"O Numero {numero} é Impar")
        print("==============================================")

Verificacao_numero_impar_par()