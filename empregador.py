########################################################################################################################
# Importando bibliotecas que vão ser utilizadas
import registro as rh

########################################################################################################################

########################################################################################################################
# Criando o menu de opções.
menu = f"""|--Menu--|
1-Cadastrar funcionário.
2-Alterar cadastro
3-Lista de funcionários
4-Desligamento de funcionário
5-Gerar advertência
6-Sair do sistema
"""
########################################################################################################################

########################################################################################################################
# Montagem do menu
while True:
    print(menu)
    select = input("Digite o número da opção desejada: ")
    if select == "1":
        rh.cadastro()
        rh.salvar()
    elif select == "2":
        rh.alterar()
        rh.salvar()
    elif select == "3":
        rh.lista()
    elif select == "4":
        rh.desligamento()
        rh.salvar()
    elif select == "5":
        rh.advertencia()
        rh.salvar()
    elif select == "6":
        break
    else:
        print("Opção inválida.")
########################################################################################################################
