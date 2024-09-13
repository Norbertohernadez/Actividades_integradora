
import tkinter as tk
from tkinter import messagebox
from LOGIN.autenticacion import Auth  

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")

        self.auth = Auth()

        
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Nombre de Usuario").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Contraseña").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(self.login_frame, text="Registrar", command=self.register)
        self.register_button.pack(pady=5)

        # Bind the Enter key to the login function
        self.root.bind('<Return>', self.login_with_enter)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth.login(username, password):
            self.show_message("Inicio de Sesión", "¡Bienvenido a VideoGames!")
        else:
            self.show_message("Inicio de Sesión", "¡Inicio de sesión fallido!")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.auth.register(username, password):
            self.show_message("Registro", "¡Registro exitoso!")
        else:
            self.show_message("Registro", "¡El usuario ya existe o entrada inválida!")

    def show_message(self, title, message):
        # Show a message box
        messagebox.showinfo(title, message)
        # Clear the entries
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        # Wait for a key press to close the message box
        self.root.bind('<Key>', self.on_key_press)

    def on_key_press(self, event):
        # Unbind the key press event
        self.root.unbind('<Key>')
        # Optionally, you could add code here to do something after the key press

    def login_with_enter(self, event):
        self.login()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
