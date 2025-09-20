velocidade = int(input("Digite a velocidade de download: "))
if velocidade < 10: 
    print("Conexão ")
else:
    if velocidade > 10 and velocidade <= 100:
        print("Conexão normal")

