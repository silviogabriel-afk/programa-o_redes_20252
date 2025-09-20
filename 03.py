endereco_ip = input("Digite o endereço IP: ")
octetos_ip = endereco_ip.split(" . ")
if len(octetos_ip) != 4:
    print("Não é IP válido")
    exit(1)
if int(octetos_ip[0]) == 192 and int(octetos_ip[1]) == 168 and int(octetos_ip[2]) == 1:
    print("Pertence a rede")