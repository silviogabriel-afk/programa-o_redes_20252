#Importa o modulo socket
import socket

#Cria o objeto socket do tipo IPV4 ou TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Estabelece conexão com o servidor que está operado na porta 5000
cliente.connect(("Localhosts", 5000))

#O cliente envia uma mensagem para o servidor
cliente.sendall("Mensagem do cliente". encode())

#O cliente 
mensagemservidor = cliente.recv(1024)

print(mensagemservidor. decode())

cliente.close()

