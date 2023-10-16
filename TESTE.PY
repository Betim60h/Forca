import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    palavraChave = input("Digite a palavra chave: ").upper()
    quantidadeDeLetras = len(palavraChave)
    dicaUm = input("Digite a primeira dica: ")
    dicaDois = input("Digite a Segunda dica: ")
    dicaTres = input("Digite a Terceira dica: ")
    dicones = [dicaUm, dicaDois, dicaTres]
    clear()
    print("----------------------------")
    print(f"A palavra chave tem {quantidadeDeLetras} letras")
    print("----------------------------")
    erros = 0
    numeroDicas = 0
    forca = ["_" if letra != " " else " " for letra in palavraChave]

    while erros < 6:
        print(" ".join(forca))
        print("[1] Digite 1 para escrever uma letra")
        print("[2] Digite 2 para pedir uma dica")
        Play = input("Digite: ")

        if Play == '1':
            clear()
            print(" ".join(forca))
            Letra = input("Escreva uma letra: ").upper()

            if Letra in palavraChave:
                print("Possui essa letra")
                time.sleep(2)
                for i in range(len(palavraChave)):
                    if palavraChave[i] == Letra:
                        forca[i] = Letra
            else:
                erros += 1
                print(f"A letra '{Letra}' não está na palavra-chave. Erros: {erros}/6")
                time.sleep(2)

        elif Play == '2':
            if numeroDicas < len(dicones):
                clear()
                print("Dica:", dicones[numeroDicas])
                numeroDicas += 1
                input("Pressione Enter para continuar...")
                clear()
            else:
                print("Você já usou todas as dicas disponíveis.")
                input("Pressione Enter para continuar...")
                clear()
        else:
            print("Opção inválida. Digite 1 para escrever uma letra ou 2 para pedir uma dica.")

    print("Fim do jogo!")
    continuar = input("Deseja jogar novamente? (S/N): ").strip().lower()
    if continuar != 's':
        break
