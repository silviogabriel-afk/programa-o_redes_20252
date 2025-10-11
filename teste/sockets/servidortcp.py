#Importar o modulo socket do python
import socket

#A função socket do modulo socket cria um objeto socket
#socket.AF_INET configura o socket para trabalhar com IPV4
#socket.SOCK_STREM configura o socket para trabalhar com TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#A função bind cria um vinculo entre uma maquina e uma porta TCP
servidor.bind(("Localhost", 5000))

#A função listen habilita o socket a ouvir pedidos de conexão
servidor.listen()

print("Esperando uma conexão!!!!")

#A função accept aceita conexões devolvendo um objeto de conexão com o cliente e o endereço do cliente
conn, address = servidor.accept()

print("Endereço do cliente: ", address)

#A função recv recebe mensagens do cliente conectado (até 1024 bytes ou valor configurado)
mensagem = conn.recv(1024)
print("Mensagem recebida: ", mensagem.decode())

#A função sendall enviar uma mensagem para o cliente
conn.sendall("Mensagem recebida com sucesso". encode())

#Fecha a conexão com o cliente
conn.close()
#Encerra o serviço do servidor
servidor.close()

