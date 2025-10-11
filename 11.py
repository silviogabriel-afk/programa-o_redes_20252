import os 

path = r"D:\Programacao20252\lista1>"

arquivos = os.listdir(path)

for arquivo in arquivos:
    if arquivo[-4:] == ".txt":
        print(arquivo)