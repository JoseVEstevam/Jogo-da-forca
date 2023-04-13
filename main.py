from palavras import Jogo, Palavra
import os

    
def main():
    while True:
        jogo = Jogo()
        while not jogo.valido:
                jogo.escolhas._apresentacao_escolha()
                jogo.valido = jogo.escolhas.valido
                jogo.parar = jogo.escolhas.parar
                if not jogo.parar and jogo.valido:
                    jogo.tema = jogo.escolhas.tema_escolhido
                    jogo.palavra_escolhida = Palavra(jogo.escolhas.palavra_escolhida)
                if jogo.parar:
                    break
        if jogo.parar:
            break
        while True:
            os.system('cls')
            jogo.forca()
            if jogo.erros >= 6:
                input("Pressione enter")
                os.system('cls')
                break
            if jogo.palavra_escolhida.vitoria():
                input("Pressione enter")
                os.system('cls')
                break  
            while True:
                letra = input("    Digite uma letra: ").lower().strip()
                if len(letra) >= 1:
                    letra = letra[0]
                    if letra not in jogo.palavra_escolhida.dicionario:
                         continue
                else:
                    print('    Digite apenas letras!')
                    continue
                break
            jogo.erros += jogo.palavra_escolhida.atualizacao(letra)


    

if __name__ == '__main__':    
        main()
