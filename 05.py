portas_comuns = [80, 443, 22, 21]

porta = int(input("Digite uma porta TCP"))
if porta in portas_comuns:
    print(f"{porta} é uma porta comum")
else:
    print(f"{porta} não é i,a porta comum")