print("========================================================================================")
print("Digite dois numeros, e apos isso digite a operação matematica desejada ( + / - / x / % )")
print("========================================================================================")
while True:
    primeiro_numero = int(input("Digite o primeiro numero:"))
    print("========================================================================================")
    operacao_desejada = input("Digite a operação desejada ( + / - / x / % ): ")
    print("========================================================================================")
    segundo_numero = int(input("Digite o segundo numero:"))
    
    def somar_dois_numeros():
        valor_final = primeiro_numero + segundo_numero
        print("========================================================================================")
        print(f"O resultado de {primeiro_numero} mais {segundo_numero} é {valor_final}")
        print("========================================================================================")
        
    def subtrair_dois_numeros():
        valor_final = primeiro_numero - segundo_numero
        print("========================================================================================")
        print(f"O resultado de {primeiro_numero} menos {segundo_numero} é {valor_final}")
        print("========================================================================================")
        
    def dividir_dois_numeros():
        valor_final = primeiro_numero / segundo_numero
        print("========================================================================================")
        print(f"O resultado de {primeiro_numero} dividido por {segundo_numero} é {valor_final}")
        print("========================================================================================")

    def multiplicar_dois_numeros():
        valor_final = primeiro_numero * segundo_numero
        print("========================================================================================")
        print(f"O resultado de {primeiro_numero} vezes {segundo_numero} é {valor_final}")
        print("========================================================================================")
        
    def verificar_operador():
        if(operacao_desejada == "-"):
            subtrair_dois_numeros()
        elif(operacao_desejada == "+"):
            somar_dois_numeros()
        elif(operacao_desejada == "x"):
            multiplicar_dois_numeros()
        elif(operacao_desejada == "%"):
            dividir_dois_numeros()
        else:
            print("========================================================================================")
            print("Parece que vc digitou uma operaçaõ diferente")
            print("========================================================================================")
    
    verificar_operador()
    continuacao = input("Deseja continuar? ( Sim / Nao): ")
    print("========================================================================================")
    if(continuacao == "Nao" or continuacao == "nao" or continuacao == "NAO" or continuacao =="n" or continuacao == "N"):
        break
    
