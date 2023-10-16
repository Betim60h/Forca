import os
import time

def clear():
    os.system("cls")
clear ()

desafiante = input("Desafiante: ")
desafiado = input("Desafiado: ")
pontuacaoDesafiante = 0
pontuacaoDesafiado = 0
while True:
        palavraChave = input(f"{desafiante} Digite a palavra chave: ").upper () 
        quantidadeDeLetras = len(palavraChave)
        dicaUm = input("Digite a primeira dica: ")
        dicaDois = input("Digite a Segunda dica: ")
        dicaTres = input("Digite a Terceira dica: ")
        dicones = [dicaUm, dicaDois, dicaTres]
        clear ()
        print("----------------------------")
        print(f"A palavra chave tem {quantidadeDeLetras} letras")
        print("----------------------------")
        erros = 0
        numeroDicas = 0
        forca = ["_" if letra != " " else " " for letra in palavraChave]
        while erros < 6:
            print(" ".join(forca))
            print ("[1] Digite 1 para escrever uma letra")
            print ('[2] Digite 2 para pedir uma dica')
            Play = input("Digite: ")
            if Play == '1':
                clear ()
                print(" ".join(forca))
                Letra = input ("escreva uma letra: ").upper ()
                if Letra in palavraChave:
                    print("Possui essa letra")
                    time.sleep(2)
                    for i in range(len(palavraChave)):
                        if palavraChave[i] == Letra:
                            forca[i] = Letra
                        clear ()
                else:
                    erros += 1
                    print ("carregando")
                    time.sleep (1)
                    print("Não possui essa letra")
                    print(f"Erros: {erros}")
                    time.sleep (1)
                    clear ()
            if "_" not in forca:
                clear()
                print("Carregando...")
                time.sleep(2)
                print(f"{desafiado} venceu, a palavra era {palavraChave}")
                pontuacaoDesafiado += 1
                time.sleep(1)
                break
            if Play == '2':
                    if numeroDicas < len(dicones):
                        dicaAtual = dicones[numeroDicas]
                        clear ()
                        print(f'Sua dica é: {dicaAtual}')
                        numeroDicas += 1
                    else:
                        print("Você já utilizou todas as suas dicas.")
        if erros == 6:
            clear()
            print(f"{desafiante} venceu, a palavra chave era:", palavraChave)
            pontuacaoDesafiante += 1
            time.sleep (2)
            clear ()
        print (f'{desafiado} {pontuacaoDesafiado} x {pontuacaoDesafiante} {desafiante}')
        opcao = input("Deseja jogar novamente? (Sim ou Não): ").lower ()
        if opcao != 'sim':
             break

