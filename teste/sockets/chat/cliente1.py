import customtkinter
from CTkMessagebox import ctkmessagebox

def conectar():
    global nome
    global cliente

    nome_valor = campo_nome.get().strip()
    if nome_valor is None or nome_valor == "":
        ctkmessagebox(title="Erro", message="Antes, digite seu nome", icon="warning")
        return

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("800x600")
janela.title("Chat IFRN Redes")

label_nome = customtkinter.CTkLabel(janela, text="Digite seu nome")
label_nome.pack(pady=(10,5))

campo_nome = customtkinter.CTkEntry(janela, width=250)
campo_nome.pack(pady=5)

botao_conectar = customtkinter.CTkButton(janela, text="Conectar", command= conectar)
botao_conectar.pack(pady=(0,10))

meno_mensagens = customtkinter.CTkTextbox(janela, width=760, height=300, state="disabled")
meno_mensagens.pack(padx=10, pady=30, fill="both", expand=True)

frame = customtkinter.CTkFrame(janela)
frame.pack(fill="x", padx=10, pady=(0,10))

campo_mensagem = customtkinter.CTkEntry(frame, state="disabled")
campo_mensagem.pack(side="left", fill="x", expand=True, padx=(0,10))

botao_enviar = customtkinter.CTkButton(frame, text="Enviar", command=None, state="disabled")
botao_enviar.pack(side="right")

cliente = None
nome = None

janela.mainloop()