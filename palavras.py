class Jogo():

    def __init__(self) -> None:
        self.escolhas = Escolhas()
        self._apresentacao()
        self.escolhas._apresentacao_escolha()
        self.erros = 0
        self.valido = self.escolhas.valido
        self.parar = self.escolhas.parar
        if not self.parar and self.valido:
            self.tema = self.escolhas.tema_escolhido
            self.palavra_escolhida = Palavra(self.escolhas.palavra_escolhida)

    def forca(self) -> None:
        if self.erros == 0:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      
     |                     
     |                     
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
     """)
        elif self.erros == 1:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      O
     |                     
     |                     
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
     """)
        elif self.erros == 2:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      O
     |                      |
     |                     
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
     """)
        elif self.erros == 3:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      O
     |                     /|
     |                     
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
     """)
        elif self.erros == 4:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      O
     |                     /|\\
     |                     
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
    """)
        elif self.erros == 5:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      O
     |                     /|\\
     |                     / 
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
     """)
        else:
            print(f"""
                                {self.tema.upper()}
     +----------------------+               {'-'.join(self.palavra_escolhida.lista_letras_usadas[1:]).upper()}
     |                      |
     |                      O
     |                     /|\\
     |                     / \\
     |
     |     
     |
     |
     |
     |  
     |    
     |      
     |        
     ============================  Palavra: {self.palavra_escolhida.palavra_junta().lower()}
    
    Resposta: {self.palavra_escolhida.palavra.title()}
      _______   _____   __    __
     |  _____| |_   _| |  \  /  |     
     | |___      | |   |   \/   |
     |  ___|     | |   | |\  /| |
     | |        _| |_  | | \/ | |
     |_|       |_____| |_|    |_|
     """)

    @staticmethod
    def _apresentacao():
        print(f'\033[34m', '~' * 60)
        print(r'''
             _    ______     _____    ______ 
            | |  /  __  \   / ____|  /  __  \ 
            | | | /    \ | | |  __  | /    \ |
         _  | | | |    | | | |  | | | |    | |
        | |_| | | \ __ / | | |__| | | \ __ / |
         \____/  \______/   \_____|  \______/ 

                 _____   
                |  __ \      /\
                | |  | |    /  \
                | |  | |   / /\ \
                | |__| |  /  __  \
                |_____/  /_/    \_\
    
     ______    ______    _____     _____  
    |  ____|  /  __  \  |  __ \   / ____|     /\
    | |__    | /    \ | | |__) | | |         /  \
    |  __|   | |    | | |  _  /  | |        / /\ \
    | |      | \ __ / | | | \ \  | |____   /  __  \
    |_|       \______/  |_|  \_\  \_____| /_/    \_\
        ''')
        print('~' * 60, '\033[m')

class Palavra():
    def __init__(self, palavra) -> None:
        self.dicionario = {
            'a': ('a', 'á', 'ä', 'à', 'ã', 'â'), 
            'e': ('e', 'é', 'ë', 'è', 'ê'), 
            'i': ('i', 'í', 'ï', 'ì', 'î'), 
            'o': ('o', 'ó', 'ö', 'ò', 'õ', 'ô'), 
            'u': ('u', 'ú', 'ü', 'ù', 'û'),
            'b': ('b'),
            'c': ('c', 'ç'), 
            'd': ('d'),
            'f': ('f'),
            'g': ('g'),
            'h': ('h'),
            'j': ('j'),
            'k': ('k'),
            'l': ('l'),
            'm': ('m'),
            'n': ('n'),
            'p': ('p'),
            'q': ('q'),
            'r': ('r'),
            's': ('s'),
            't': ('t'),
            'v': ('v'),
            'w': ('w'),
            'x': ('x'),
            'y': ('y'),
            'z': ('z'),
            ' ': (' '),
            '-': ('-')
        }
        self.palavra = palavra.lower()
        self.tamanho = len(self.palavra)
        self.lista_letras = list('_' * self.tamanho)
        self.lista_pos = []
        self.lista_letras_usadas = []
        self._verificacao_inicial()
    
    def _posicao(self, verificar) -> None:
        contador = 0
        for letra in self.palavra:
            if letra == verificar:
                self.lista_pos.append(contador)
            contador += 1

    def _verificacao_inicial(self) -> None:
        self.atualizacao('-')
        self.atualizacao(' ')

    def atualizacao(self, usuario) -> None:
        if usuario not in self.lista_letras_usadas:
            self.lista_letras_usadas.append(usuario)
            for letra in self.dicionario[usuario]:
                if letra in self.palavra:
                    self._posicao(letra)
                    for indice in self.lista_pos:
                        self.lista_letras[indice] = letra
                    self.lista_pos.clear()
                    return 0
                else:
                    return 1
        else:
            return 0

    def palavra_junta(self) -> None:
        return ''.join(self.lista_letras)

    def vitoria(self) -> None:
        if '_' not in self.lista_letras:
            print("""
    __      __  _____   _______    ______    _____    _____       
    \ \    / / |_   _| |__   __|  /  __  \  |  __ \  |_   _|     /\    
     \ \  / /    | |      | |    | /    \ | | |__) |   | |      /  \   
      \ \/ /     | |      | |    | |    | | |  _  /    | |     / /\ \  
       \  /     _| |_     | |    | \ __ / | | | \ \   _| |_   / ____ \ 
        \/     |_____|    |_|     \______/  |_|  \_\ |_____| /_/    \_\\
        """)
            return True
        else:
            return False


class Escolhas():
    def __init__(self) -> None:
        self.valido = True
        self.parar = False
        self.temas = ('Esportes', 'Comidas', 'Mar', 'Casa', 'Escola', 'Parque', 'Carro')
        self.tema = {
                    'Esportes':['Futebol', 'Basquete', 'Vôlei', 'Natação',
                    'Atletismo', 'Boxe', 'Tênis', 'Ginástica',
                    'Handebol', 'Rugby', 'Ciclismo', 'Skate',
                    'Surfe', 'Corrida', 'Artes marciais', 'Escalada',
                    'Esqui', 'Snowboard', 'Patinação', 'Remo'],
                    'Comidas':['Lasanha', 'Pizza', 'Hambúrguer', 'Sushi',
                    'Churrasco', 'Feijoada', 'Strogonoff', 'Tapioca',
                    'Pão de queijo', 'Brigadeiro', 'Coxinha', 'Empadão',
                    'Pudim', 'Quindim', 'Acarajé', 'Panqueca',
                    'Cuscuz', 'Pamonha', 'Macarronada', 'Risoto'], 
                    'Mar':['Peixe', 'Coral', 'Alga', 'Concha',
                    'Ouriço', 'Tartaruga', 'Golfinho', 'Baleia',
                    'Tubarão', 'Lula', 'Água', 'Caravela',
                    'Gaivota', 'Estrela-do-mar', 'Polvo', 'Molusco',
                    'Ostra', 'Mexilhão', 'Siri', 'Caranguejo'], 
                    'Casa':['Sala', 'Quarto', 'Banheiro', 'Cozinha',
                    'Corredor', 'Varanda', 'Jardim', 'Telhado',
                    'Escada', 'Parede', 'Teto', 'Porta',
                    'Janela', 'Cortina', 'Tapete', 'Sofá',
                    'Armário', 'Estante', 'Mesa', 'Cadeira'], 
                    'Escola':['Professor', 'Aluno', 'Quadro negro', 'Sala de aula', 
                    'Livro', 'Mochila', 'Merenda', 'Prova', 
                    'Nota', 'Caderno', 'Lousa', 'Caneta', 
                    'Borracha', 'Giz', 'Diretor', 'Secretaria', 
                    'Biblioteca', 'Laboratório', 'Ensino', 'Aprendizagem'], 
                    'Parque':['Árvore', 'Gramado', 'Banco', 'Pista de caminhada', 
                    'Playground', 'Ciclovia', 'Piquenique', 'Trilha', 
                    'Lago', 'Escorregador', 'Balanço', 'Patins', 
                    'Skate', 'Bicicleta', 'Parquinho', 'Descanso', 
                    'Quadra esportiva', 'Criança', 'Esportes', 'Diversão'],
                    'Carro':['Volante', 'Motor', 'Rodas', 'Assento',
                    'Cinto de segurança', 'Freio', 'Marcha', 'Porta-malas',
                    'Farol', 'Buzina', 'Espelho retrovisor', 'Tanque de combustível',
                    'Para-brisa', 'Ar condicionado', 'GPS', 'Rádio',
                    'Câmbio', 'Vidro', 'Ignição', 'Suspensão']}
        self.tema_escolhido:str
        self.palavra_escolhida:str

    def _escolha_aleatorio(self):
        from random import randint
        self.tema_escolhido = self.temas[randint(0, 6)]
        self._escolha_palavra()
    
    def _escolha_manual(self):
        while True:
            resposta = input(f'''
    Digite o número correspondente ao tema escolhido:
    {"Esportes":-<25} 0
    {"Comidas":-<25} 1
    {"Mar":-<25} 2
    {"Casa":-<25} 3
    {"Escola":-<25} 4
    {"Parque":-<25} 5
    {"Carro":-<25} 6
    Sua escolha: ''')
            try:
                inteiro = int(resposta)
            except:
                print('''
    Insira um valor inteiro!''')
            else:
                if inteiro in range(0, 7):
                    self.tema_escolhido = self.temas[inteiro]
                    self._escolha_palavra()
                    return

    def _escolha_palavra(self):
        from random import randint
        self.palavra_escolhida = self.tema[self.tema_escolhido][randint(0, 19)]

    def _apresentacao_escolha(self):
        resposta = input(f'''
    {'-'*60}
    MENU:
    Digite 1 - Iniciar o jogo com escolha aletória do tema
    Digite 2 - Iniciar o jogo com escolha manual do tema
    Digite 3 - Para sair do jogo

    Opção: ''')
        try:
                resposta = int(resposta)
        except:
                print('''
    Apenas valores inteiros são aceitos!''')
                self.valido = False
        else:
            if resposta == 1:
                escolha = self._escolha_aleatorio()
                self.valido = True
            elif resposta == 2:
                escolha = self._escolha_manual()
                self.valido = True
            elif resposta == 3:
                print('    Obrigado por jogar!')
                self.parar = True
            else:
                print('''
    Digite o valor correspondente!''')
                self.valido = False


if __name__ == '__main__':
    teste = Jogo()
