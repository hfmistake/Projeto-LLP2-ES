from tkinter import *


def perfil(fun):
    ####################################################################################################################
    # Formatando as datas recebidas
    c_format = str(fun.data_contrato.day).zfill(2) + "/" \
               + str(fun.data_contrato.month).zfill(2) + "/" + str(fun.data_contrato.year).zfill(4)

    n_format = str(fun.data_nasc.day).zfill(2) + "/" \
               + str(fun.data_nasc.month).zfill(2) + "/" + str(fun.data_nasc.year).zfill(4)
    ####################################################################################################################
    # Janela de perfil
    profile = Tk()
    profile.geometry("800x500")
    profile.resizable(width=False, height=False)
    profile.title(fun.nome)
    profile.iconbitmap(default="images\\rh.ico")
    ####################################################################################################################

    ####################################################################################################################
    # Upload de fotos
    user_photo = PhotoImage(file="images\\user.png")
    ####################################################################################################################

    ####################################################################################################################

    ####################################################################################################################
    # Labels
    bg = Label(profile, width=800, height=500, bg="White", anchor="center")
    frame = LabelFrame(bg, text="Perfil", bg="gray", labelanchor="n", font=("Fira Code", 18),
                       highlightbackground="black",
                       highlightthickness=6)
    foto = Label(frame, image=user_photo, bg="white", text="FOTO", anchor="n", font=("Fira Code", 18),
                 compound="bottom",
                 highlightbackground="black", highlightthickness=5, fg="blue")
    bg.place(width=800, height=500)
    frame.pack(fill="both", expand=1)
    foto.pack(anchor="nw")
    ####################################################################################################################
    ####################################################################################################################
    # Info Frames
    name = LabelFrame(frame, text="NOME", font=("Fira Code", 10), width=450, height=50, labelanchor="n",
                      highlightbackground="black", highlightthickness=2)
    ender = LabelFrame(frame, text="ENDEREÇO", font=("Fira Code", 10), width=450, height=50, labelanchor="n",
                       highlightbackground="black", highlightthickness=2)
    cargo = LabelFrame(frame, text="CARGO", font=("Fira Code", 10), width=180, height=50, labelanchor="n",
                       highlightbackground="black", highlightthickness=2)
    cpf = LabelFrame(frame, text="CPF", font=("Fira Code", 10), width=180, height=50, labelanchor="n",
                     highlightbackground="black", highlightthickness=2)
    idade = LabelFrame(frame, text="IDADE", font=("Fira Code", 10), width=70, height=50, labelanchor="n",
                       highlightbackground="black", highlightthickness=2)
    nasc = LabelFrame(frame, text="DATA DE NASCIMENTO", font=("Fira Code", 10), width=180, height=50, labelanchor="n",
                      highlightbackground="black", highlightthickness=2)
    contrato = LabelFrame(frame, text="DATA DE CONTRATO", font=("Fira Code", 10), width=180, height=50, labelanchor="n",
                          highlightbackground="black", highlightthickness=2)
    senha = LabelFrame(frame, text="SENHA", font=("Fira Code", 10), width=70, height=50, labelanchor="n",
                       highlightbackground="black", highlightthickness=2)
    status = LabelFrame(frame, text="STATUS", font=("Fira Code", 10), width=180, height=50, labelanchor="n",
                        highlightbackground="black", highlightthickness=2)
    cracha = LabelFrame(frame, text="CRACHÁ", font=("Fira Code", 10), width=70, height=50, labelanchor="n",
                        highlightbackground="black", highlightthickness=2)
    adv = LabelFrame(frame, text="ADVERTENCIAS", font=("Fira Code", 10), width=180, height=50, labelanchor="n",
                     highlightbackground="black", highlightthickness=2)

    name.place(x=300, anchor="nw")
    ender.place(x=300, y=60, anchor="nw")
    cracha.place(x=300, y=120, anchor="nw")
    adv.place(x=380, y=120, anchor="nw")
    cargo.place(x=570, y=120, anchor="nw")
    cpf.place(x=300, y=180, anchor="nw")
    idade.place(x=490, y=180, anchor="nw")
    nasc.place(x=570, y=180, anchor="nw")
    contrato.place(x=570, y=240, anchor="nw")
    senha.place(x=490, y=240, anchor="nw")
    status.place(x=300, y=240, anchor="nw")
    ####################################################################################################################

    ####################################################################################################################
    # Posicionando as informações.
    n = Label(name, text=fun.nome, font=("Fira Code", 12), fg="blue")
    e = Label(ender, text=fun.endereco, font=("Fira Code", 12), fg="blue")
    c = Label(cracha, text=str(fun.cracha), font=("Fira Code", 12), fg="blue")
    a = Label(adv, text=str(fun.advertencias), font=("Fira Code", 12), fg="blue")
    carg = Label(cargo, text=fun.cargo, font=("Fira Code", 12), fg="blue")
    t_cpf = Label(cpf, text=fun.cpf, font=("Fira Code", 12), fg="blue")
    i = Label(idade, text=str(fun.idade), font=("Fira Code", 12), fg="blue")
    nn = Label(nasc, text=n_format, font=("Fira Code", 12), fg="blue")
    s = Label(status, text=fun.status, font=("Fira Code", 12), fg="blue")
    ss = Label(senha, text=fun.senha, font=("Fira Code", 12), fg="blue")
    dc = Label(contrato, text=c_format, font=("Fira Code", 12), fg="blue")
    n.place(x=220, y=10, anchor="center")
    e.place(x=220, y=10, anchor="center")
    c.place(x=30, y=10, anchor="center")
    a.place(x=85, y=10, anchor="center")
    carg.place(x=90, y=10, anchor="center")
    t_cpf.place(x=85, y=10, anchor="center")
    i.place(x=30, y=10, anchor="center")
    nn.place(x=80, y=10, anchor="center")
    s.place(x=85, y=10, anchor="center")
    ss.place(x=30, y=10, anchor="center")
    dc.place(x=80, y=10, anchor="center")
    ####################################################################################################################

    # Rodar a janela
    profile.mainloop()
