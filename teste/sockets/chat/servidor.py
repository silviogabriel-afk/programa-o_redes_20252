import socket
import threading

clientes = []

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 5000))
    servidor.listen()

    while True:
        #A variavel "cliente" corresponde a uma conexão aberta com o servidor
        cliente, endereco = servidor.accept()
        clientes.append(cliente)
        thread = threading.Thread(target= tratar_mensagens_cliente, args=(cliente, endereco))
        thread.start()

def tratar_mensagens_cliente(cliente, endereco):
    while True:
        try:
            mensagem_bytes = cliente.recv(10000)
            if mensagem_bytes:
                enviar_mensagem_clientes(mensagem_bytes, cliente)
        except Exception as e:
            print("Erro na recepção de mensagem:", e)

def enviar_mensagem_clientes(mensagem, cliente_origem):
    for cliente in cliente:
        try:
            if cliente != cliente_origem:
                cliente.send(mensagem)
        except Exception as e:
            print("Erro no envio de mensagem:", e)

iniciar_servidor()
