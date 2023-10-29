import login
import sys
import time

while True:
    if fun := login.start():  # Utilização do "walrus operator" permite atribuir valor a uma variavel enquanto roda o
        # "if".
        print(f"Seja bem vindo ao sistema!\nFuncionário:{str(fun.cracha).zfill(2)}-{fun.nome}")
        time.sleep(5)
        print("\nPor enquanto faremos só ate essa parte. Que venha Programação orientada a objetos!")
        time.sleep(3)
        print("Encerrando o sistema em:", end=" ", flush=True)
        print("3...", end="", flush=True)
        time.sleep(1)
        print("2...", end="", flush=True)
        time.sleep(1)
        print("1...", end="", flush=True)
        time.sleep(1)
        print("Até 2023!", flush=True)
        time.sleep(5)
        sys.exit()
    else:
        print("O login não foi completado.")
        while True:
            retry = input("1-Tentar novamente\n2-Encerrar\nSelecione uma opção: ")
            if retry == "1":
                break
            elif retry == "2":
                sys.exit()
            else:
                print("\nOpção inválida! Digite novamente.")
