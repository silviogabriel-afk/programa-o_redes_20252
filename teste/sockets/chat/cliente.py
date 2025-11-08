import customtkinter

customtkinter.set_apperance_mode("dark")
customtkinter.set_dafault_color_theme("green")

def button_callback():
    print("Button clicked")

app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text= "my button", comand=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()

