print("==========================================================")
print("Digite um numero e veja a tabuada completa")
print("==========================================================")

numero = int(input("Digite um numero: "))
print("=========================================================")

def verificar_tabuada():
    for i in range(1,11):
        valor_multiplicacao = numero*i
        print(f"{numero} x {i} = {valor_multiplicacao}")
    
    
verificar_tabuada()