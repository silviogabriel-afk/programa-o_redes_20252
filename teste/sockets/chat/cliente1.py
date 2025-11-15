import customtkinter
from CTkMessagebox import CTkMessagebox
import socket
import threading

def enviar_mensagem():
    global cliente
    global nome

    mensagem = campo_mensagem.get().strip()
    if not mensagem:
        return
    
    mensagem = f"[{nome}] {mensagem}"
    campo_mensagem.delete(0, "end")

    try:
        cliente.send(mensagem.encode())
        memo_mensagens.configure(state = "normal")
        memo_mensagens.insert("end", mensagem + "\n")
        memo_mensagens.see("end")
        memo_mensagens.configure(state = "disabled")
    except Exception as e:
        CTkMessagebox(title="Erro", message="Erro no envio de mensagem", icon="warning")


def receber_mensagem():
    global cliente 

    while True:
        try:
            mensagem = cliente.recv(10000).decode()
            memo_mensagens.configure(state = "normal")
            memo_mensagens.insert("end", mensagem + "\n")
            memo_mensagens.see("end")
            memo_mensagens.configure(state = "disabled")
        except Exception as e:
            pass

def conectar():
    global nome
    global cliente

    nome_valor = campo_nome.get().strip()
    if nome_valor is None or nome_valor == "":
        CTkMessagebox(title="Erro", message="Antes, digite seu nome", icon="warning")
        return    
    
    nome = nome_valor

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(("10.209.1.28", 5000))

        campo_mensagem.configure(state = "normal")
        botao_enviar.configure(state = "normal")
        botao_conectar.configure(state = "disabled")
        campo_nome.configure(state = "disabled")

        thread = threading.Thread(target=receber_mensagem)
        thread.start()

    except Exception as e:
        CTkMessagebox(title="Erro", message="Erro na conexão", icon="warning")
    


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("800x600")
janela.title("Chat IFRN Redes")

label_nome = customtkinter.CTkLabel(janela, text="Digite seu nome")
label_nome.pack(pady=(10,5))

campo_nome = customtkinter.CTkEntry(janela, width=250)
campo_nome.pack(pady=5)

botao_conectar = customtkinter.CTkButton(janela, text="Conectar", command = conectar)
botao_conectar.pack(pady=(0,10))

memo_mensagens = customtkinter.CTkTextbox(janela, width=760, height=300, state="disabled")
memo_mensagens.pack(padx=10, pady=30, fill="both", expand=True)

frame = customtkinter.CTkFrame(janela)
frame.pack(fill="x", padx=10, pady=(0,10))

campo_mensagem = customtkinter.CTkEntry(frame, state="disabled")
campo_mensagem.pack(side="left", fill="x", expand=True, padx=(0,10))

def funcao_campo_mensagem_enter(event = None):
    enviar_mensagem

campo_mensagem.bind("return", funcao_campo_mensagem_enter)

botao_enviar = customtkinter.CTkButton(frame, text="Enviar", command=enviar_mensagem, state="disabled")
botao_enviar.pack(side="right")

cliente = None
nome = None

janela.mainloop()
