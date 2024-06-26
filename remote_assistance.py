import tkinter as tk
from tkinter import messagebox, CENTER
import subprocess

# Função para executar o comando MSRA como administrador
def run_as_admin():
    computername = entry_computer.get()

    # Verifica se o campo do nome do computador está vazio
    if not computername:
        messagebox.showwarning("Atenção", "Por favor, insira o nome do computador.")
        return

    # Comando que será executado no CMD como administrador
    cmd = f'msra /offerra {computername}'

    try:
        # Executa o CMD sem abrir uma janela visível
        subprocess.Popen(['cmd', '/c', cmd], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Falha ao abrir o MSRA: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Remote Access MSRA")  # Define o título da janela

# Obtém a largura e altura da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define as novas dimensões da janela
window_width = 300
window_height = 250

# Calcula a posição central da janela
position_x = int(screen_width / 2 - window_width / 2)
position_y = int(screen_height / 2 - window_height / 2)

# Define a geometria da janela
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Cria um frame para o formulário e centraliza na janela
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Label e campo de entrada para o nome do computador
tk.Label(frame, text="Computer Name:").pack(pady=5)
entry_computer = tk.Entry(frame)
entry_computer.pack(pady=5)
entry_computer.focus()  # Define o foco inicial no campo do nome do computador

# Função para vincular a tecla Enter ao botão Conectar
def bind_enter(event):
    run_as_admin()

# Vincula a tecla Enter ao botão Conectar
root.bind('<Return>', bind_enter)

# Botão Conectar
btn_conectar = tk.Button(frame, text="Conectar", command=run_as_admin)
btn_conectar.pack(pady=10)

# Inicia a interface gráfica
root.mainloop()
