nota1 = float(input("Digite a primeira nota: "))                                  
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))                               
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    verificao_nota_final = (f"Parabéns, você foi aprovado com {media:.1f} Pontos")
else:
    verificao_nota_final = (f"Infelizmente você ficou com {media:.1f} Pontos, e terá que fazer a recuperação")

print("================================")
print(verificao_nota_final)
print("================================")