print("====================================================")
print("Digite uma temperatura, e depois converta para Fahrenheit ou Celsius")
print("====================================================")

temperatura = float(input("Digite a temperatura: "))
print("====================================================")
unidade_medida = int(input("Converter para ( 1 - Fahrenheit / 2 - Celsius): "))

def converter_temperatura():
    if (unidade_medida == 1):
        conversao = ((temperatura * 9) / 5) + 32
        print("====================================================")
        print(f"Resultado: {conversao:.2f} Graus Fahrenheit")
        print("====================================================")
    elif(unidade_medida == 2):
        conversao = ((temperatura - 32) * 5) / 9 
        print("====================================================")
        print(f"Resultado: {conversao:.4f} Graus Celsius")
        print("====================================================")
        
converter_temperatura()
