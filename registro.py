########################################################################################################################
# Importando bibliotecas que vão ser utilizadas
from dataclasses import dataclass
import profile as pf
import datetime
import pickle
import re

########################################################################################################################


########################################################################################################################
# Criação da classe
@dataclass
class Funcionario:
    cracha: int = 0
    nome: str = ""
    data_nasc: datetime.date = datetime.date(1, 1, 1)
    endereco: str = ""
    cpf: str = ""
    cargo: str = ""
    senha: str = ""
    idade: int = 0
    data_contrato: datetime.date = datetime.date.today()
    status: str = "Ativo"
    advertencias: int = 0


########################################################################################################################

########################################################################################################################
# Função de cadastro.
def cadastro():
    fun = Funcionario()
    fun.cracha = len(funcionarios) + 1
    fun.nome = pegar_nome()
    fun.data_nasc = pegar_nasc()
    fun.endereco = pegar_endereco()
    fun.cpf = pegar_cpf()
    fun.senha = fun.cpf[7:]
    fun.cargo = pegar_cargo()
    fun.idade = calculo_idade(fun)
    if confirmar(fun, "cadastro"):
        funcionarios.append(fun)
        print(f"Funcionário de crachá: {fun.cracha} cadastrado com sucesso!")
    else:
        print("O funcionário não foi cadastrado.")


########################################################################################################################

########################################################################################################################
# Função exibir menu de confirmação para alterações importantes.
def confirmar(fun, tipo):
    info = f"""
    Crachá: {fun.cracha}
    Nome: {fun.nome}
    Data de nascimento: {fun.data_nasc.day}/{fun.data_nasc.month}/{fun.data_nasc.year}
    Endereço: {fun.endereco}
    CPF: {fun.cpf}
    Cargo: {fun.cargo}
    Senha: {fun.senha}
    Idade: {fun.idade}
    """
    print(info)
    while True:
        confirm = input(f"\nConfirmar {tipo}? [S]-Sim ou [N]-Não\nConfirmar?:")
        if confirm.upper() == "S":
            return True
        elif confirm.upper() == "N":
            return False
        else:
            print("Opção inválida! Leia as instruções e digite novamente.")


########################################################################################################################

########################################################################################################################
# Funções para obter as informações com validação.
def pegar_nome():  # Obter nome com validação usando "regexes" e recursion call.
    nome = input("Informe o nome completo: ").title()
    if re.search("^([a-zA-zà-üÀ-Ü]+ [a-zA-zà-üÀ-Ü]+)+$", nome):
        return nome
    else:
        print("Nome inválido. Digite novamente.")
        return pegar_nome()


def pegar_nasc():  # Obter data de nascimento com validação usando map,list comprehensions e recursion call.
    data = input("Informe a data de nascimento. Formato = [dd/mm/aaaa]: ").split("/")
    if len(data) == 3 and len([r for r in map(str.isdigit, data) if r is True]) == 3:  # Validação da data
        dia, mes, ano = data
        data_nasc = datetime.date(day=int(dia), month=int(mes), year=int(ano))
        return data_nasc
    else:
        print("Data inválida. Digite novamente.")
        return pegar_nasc()


def pegar_endereco():
    endereco = input("Informe o endereço: ")
    if endereco:
        return endereco
    else:
        print("Endereço inválido. Digite novamente.")
        return pegar_endereco()


def pegar_cpf():  # Obter CPF com validação usando recursion call.
    cpf = input("Informe o CPF: ")
    if cpf.isdigit() and len(cpf) == 11:  # Certificando que o cpf inserido são numeros e tem o tamanho 11.
        return cpf
    else:
        print("CPF inválido. Digite novamente.")
        return pegar_cpf()


def pegar_cargo():  # Obter o cargo de ocupação com um menu de escolhas.
    cargos = ["Auxiliar Administrativo", "Auxiliar de Escritório", "Analista de Logística", "Vendedor", "Zelador",
              "Supervisor", "Gerente", "Estagiário"]
    print("\n    Lista de cargos:")
    for cont, cargo in enumerate(cargos):
        print(f"    {cont + 1}-{cargo}")

    print(f"    9-Inserir cargo manualmente.")
    while True:
        try:
            select = int(input("\nSelecione o cargo de ocupação: "))
            if select == 9:
                cargo = input("Informe o cargo: ")
                break
            else:
                cargo = cargos[select - 1]
                break
        except IndexError:
            print("Cargo inválido! Digite novamente.")
    return cargo


def calculo_idade(fun):  # Calcular a idade com base na data de nascimento.
    dia_atual = datetime.date.today()
    data_nasc = fun.data_nasc
    idade = dia_atual.year - data_nasc.year - ((dia_atual.month, dia_atual.day) < (data_nasc.month, data_nasc.day))
    return idade


########################################################################################################################

########################################################################################################################
# Função de alteração no cadastro.
def alterar(repeat=False):
    if repeat is False:
        lista("3", tipo="alterar")
    encontrou = False
    identify = int(input("\nDigite o número do crachá do funcionário para alterar o cadastro: "))
    for fun in funcionarios:
        if identify == fun.cracha:
            b_nome = fun.nome
            b_data_nasc = fun.data_nasc
            b_endereco = fun.endereco
            b_cargo = fun.cargo
            b_cpf = fun.cpf
            encontrou = True
            while True:
                info = f'''
    1-Nome: {fun.nome}
    2-Data de nascimento: {fun.data_nasc.day}/{fun.data_nasc.month}/{fun.data_nasc.year}
    3-Endereço: {fun.endereco}
    4-Cargo: {fun.cargo}
    5-CPF: {fun.cpf}
    0-Finalizar alteração
    '''
                print(info)

                select = input("Digite o número da informação que deseja alterar: ")
                if select == "0":
                    if confirmar(fun, tipo="alteração"):
                        print("Alteração efetuada!")
                    else:
                        fun.nome = b_nome
                        fun.data_nasc = b_data_nasc
                        fun.endereco = b_endereco
                        fun.cargo = b_cargo
                        fun.cpf = b_cpf
                        fun.senha = b_cpf[7:]
                        print("Alteração não efetuada!")
                    break
                elif select == "1":
                    fun.nome = pegar_nome()
                elif select == "2":
                    fun.data_nasc = pegar_nasc()
                elif select == "3":
                    fun.endereco = pegar_endereco()
                elif select == "4":
                    fun.cargo = pegar_cargo()
                elif select == "5":
                    fun.cpf = pegar_cpf()
                    fun.senha = fun.cpf[7:]
                else:
                    print("Opção invalida!. Digite novamente.")
    if encontrou is False:
        print("Número do crachá inválido! Digite novamente.")
        alterar(True)


########################################################################################################################

########################################################################################################################
# Função para exibir lista de funcionários ativos ou desligados. Com opção de acessar perfil específico.
def lista(select=None, tipo="perfil"):
    if select is None:
        select = input("1-Lista de Ativos\n2-Lista de Desligados\n3-Lista Geral\nQual lista deseja consultar?: ")
    if select == "1":
        print(f"|{'Crachá':^6}|{'Idade':^5}|{'Nome':^50}|{'Cargo':^30}|{'Data de Contrato':^16}|")
        for fun in funcionarios:
            if fun.status == "Ativo":
                d_format = str(fun.data_contrato.day).zfill(2) + "/" \
                           + str(fun.data_contrato.month).zfill(2) + "/" + str(fun.data_contrato.year).zfill(4)
                print(f"|{fun.cracha:^6}|{fun.idade:^5}|{fun.nome:^50}|{fun.cargo:^30}|{d_format:^16}|")
        if tipo == "perfil":
            per(1)

    elif select == "2":
        print(f"|{'Crachá':^6}|{'Idade':^5}|{'Nome':^50}|{'Cargo':^30}|{'Data de Contrato':^16}|")
        for fun in funcionarios:
            if fun.status == "Desligado":
                d_format = str(fun.data_contrato.day).zfill(2) + "/" \
                           + str(fun.data_contrato.month).zfill(2) + "/" + str(fun.data_contrato.year).zfill(4)
                print(f"|{fun.cracha:^6}|{fun.idade:^5}|{fun.nome:^50}|{fun.cargo:^30}|{d_format:^16}|")
        if tipo == "perfil":
            per(2)
    elif select == "3":
        print(f"|{'Crachá':^6}|{'Idade':^5}|{'Nome':^50}|{'Cargo':^30}|{'Data de Contrato':^16}|")
        for fun in funcionarios:
            d_format = str(fun.data_contrato.day).zfill(2) + "/" \
                       + str(fun.data_contrato.month).zfill(2) + "/" + str(fun.data_contrato.year).zfill(4)
            print(f"|{fun.cracha:^6}|{fun.idade:^5}|{fun.nome:^50}|{fun.cargo:^30}|{d_format:^16}|")
        if tipo == "perfil":
            per(3)
    else:
        print("Opção inválida. Digite novamente!")
        lista()


########################################################################################################################

########################################################################################################################
# Função para abrir a interface de perfil de funcionário.
def per(tipo):
    if tipo == 1:
        while True:
            found = False
            perfil = input("\nDigite o número de crachá do funcionário para acessar o perfil completo. Ou [0] para "
                           "voltar ao menu principal: ")
            if perfil == "0":
                return None
            else:
                for fun in funcionarios:
                    if perfil == str(fun.cracha) and fun.status == "Ativo":
                        found = True
                        pf.perfil(fun)
            if found is False:
                print("Crachá inválido. Digite novamente.\n")
    if tipo == 2:
        while True:
            found = False
            perfil = input("\nDigite o número de crachá do funcionário para acessar o perfil completo. Ou [0] para "
                           "voltar ao menu principal: ")
            if perfil == "0":
                return None
            else:
                for fun in funcionarios:
                    if perfil == str(fun.cracha) and fun.status == "Desligado":
                        found = True
                        pf.perfil(fun)
            if found is False:
                print("Crachá inválido. Digite novamente.\n")
    if tipo == 3:
        while True:
            found = False
            perfil = input("\nDigite o número de crachá do funcionário para acessar o perfil completo. Ou [0] para "
                           "voltar ao menu principal: ")
            if perfil == "0":
                return None
            else:
                for fun in funcionarios:
                    if perfil == str(fun.cracha):
                        found = True
                        pf.perfil(fun)
            if found is False:
                print("Crachá inválido. Digite novamente.\n")


########################################################################################################################

########################################################################################################################
# Função que vai carregar o arquivo de dados para o programa.
def carregar():
    global funcionarios
    try:
        with open("funcionarios", "rb") as arquivo:
            funcionarios = pickle.load(arquivo)
    except FileNotFoundError:
        createfile = open("funcionarios", "w")
        createfile.close()
        carregar()
        print("O arquivo de dados foi criado automaticamente.")
    except EOFError:
        print("O arquivo de dados está vazio.")
    for fun in funcionarios:  # Atualização da idade toda vez q o arquivo é carregado.
        fun.idade = calculo_idade(fun)


########################################################################################################################

########################################################################################################################
# Função que vai salvar(escrever) os dados do programa no arquivo
def salvar():
    global funcionarios
    with open("funcionarios", "wb") as arquivo:
        pickle.dump(funcionarios, arquivo)


########################################################################################################################
# Função para desligamento de funcionário.
def desligamento(repeat=False):
    if repeat is False:
        lista("1", tipo="desligamento")
    encontrou = False
    identify = input("\nDigite o número de crachá do funcionário para desliga-lo: ")
    for fun in funcionarios:
        if str(fun.cracha) == identify:
            print(f"Funcionário encontrado!")
            encontrou = True
            if confirmar(fun, "desligamento"):
                fun.status = "Desligado"
                print("O funcionário foi desligado!")
            else:
                print("O funcionário não foi desligado!")

    if encontrou is False:
        print("Número do crachá inválido! Digite novamente.")
        desligamento(True)


########################################################################################################################
# Função para atribuir uma advertência ao funcionário.
def advertencia(repeat=False):
    if repeat is False:
        lista("1", tipo="advertencia")
    encontrou = False
    identify = input("\nDigite o número de crachá do funcionário para adverti-lo: ")
    for fun in funcionarios:
        if str(fun.cracha) == identify:
            print(f"Funcionário encontrado!")
            encontrou = True
            if confirmar(fun, "advertencia"):
                fun.advertencias += 1
                print("O funcionário foi advertido!")
            else:
                print("O funcionário não foi advertido!")

    if encontrou is False:
        print("Número do crachá inválido! Digite novamente.")
        advertencia(True)


########################################################################################################################
# Lista contendo os funcionários cadastrados.
funcionarios = []  # Registro geral. Contendo inclusive os funcionários desligados.
carregar()
########################################################################################################################
