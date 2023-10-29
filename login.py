####################################################################################################################
# Bibliotecas
import tkinter as tk
from tkinter import messagebox
import registro as rh

####################################################################################################################

####################################################################################################################
check = False  # Responsavel por verificar se o login foi aceito ou não, e armazenar qual funcionário caso aceito.


####################################################################################################################

####################################################################################################################
# Função principal(Iniciar a janela.)
def start():
    global check

    ####################################################################################################################
    def validar_login():  # Função que vai validar a tentativa de login
        found = False
        if cc.get() == "":
            if messagebox.showinfo("Login Negado", 'Campo "Crachá" vazio.'):
                return None
        if pp.get() == "":
            if messagebox.showinfo("Login Negado", 'Campo "Senha" vazio.'):
                return None
        for fun in rh.funcionarios:
            if str(fun.cracha) == cc.get():
                found = True
                if str(fun.senha) == pp.get():
                    global check
                    check = fun
                    if messagebox.showinfo("Login Efetuado.", "Login efetuado com sucesso!"):
                        return janela.destroy()
                else:
                    if messagebox.showinfo("Login Negado", "Senha incorreta!"):
                        return None
        if found is False:
            if messagebox.showinfo("Login Negado", "Crachá não encontrado no sistema."):
                return None

    ####################################################################################################################

    ####################################################################################################################
    def mascara_senha():  # Função para mascara de senha
        if pp.cget(key="show") == '*':
            pp.config(show="")
        else:
            pp.config(show="*")

    ####################################################################################################################

    ####################################################################################################################
    def fechar():  # Função para exibir uma confirmação ao tentar fechar a janela.
        if messagebox.askokcancel("Fechar", "Deseja fechar a janela?"):
            janela.destroy()

    ####################################################################################################################
    # Criação de janela.
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry("500x800")
    janela.iconbitmap(default="images\\rh.ico")
    janela.resizable(width=False, height=False)

    # Importar imagens
    bt = tk.PhotoImage(file="images\\BT.png")
    img_fundo = tk.PhotoImage(file="images\\Fundo.png")

    # Label
    fundo = tk.Label(janela, image=img_fundo)
    mensagem = tk.Label(janela, text="Seja Bem Vindo! Faça o login para prosseguir.", font=("Fira Code", 15),
                        bg="black",
                        fg="orange")
    fundo.place(width=500, height=800)
    mensagem.place(width=430, height=30, x=30, y=680)

    # Caixa de entrada
    cc = tk.Entry(font=("Fira Code", 18), bg="gray", fg="orange", insertbackground="orange", cursor="hand2", )
    pp = tk.Entry(font=("Fira Code", 18), bg="gray", fg="orange", insertbackground="orange", cursor="hand2", show="*")
    cc.place(width=185, height=33, x=50, y=300)
    pp.place(width=185, height=33, x=50, y=392)

    # Botões
    login = tk.Button(janela, image=bt, bg="orange", activebackground="yellow", command=validar_login)
    m_senha = tk.Checkbutton(janela, text="Mostrar senha", bg="gray", fg="orange", selectcolor="gray",
                             command=mascara_senha)
    login.place(x=150, y=500)
    m_senha.place(x=50, y=430)

    # Montagem
    janela.protocol("WM_DELETE_WINDOW", fechar)
    cc.focus()
    janela.mainloop()
    return check
####################################################################################################################
