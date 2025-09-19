# -------------------------------
# Função para validar números inteiros dentro de um intervalo
# -------------------------------
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


# -------------------------------
# Função para calcular o fatorial
# -------------------------------
def fatorial(num):
    """
    Calcula o fatorial de um número inteiro.
    :param num: número inteiro
    :return: fatorial de num
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1):
        fat *= i
    return fat


# -------------------------------
# Funções para manipulação de arquivos (Cadastro de Jogos)
# -------------------------------
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')  # tenta abrir em modo leitura
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')  # cria em modo escrita
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')  # adiciona no final do arquivo
    except:
        print('Erro ao abrir arquivo.')
    else:
        a.write(f'{nomeJogo};{nomeVideoGame}\n')
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')  # leitura
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================
if __name__ == "__main__":

    # -------------------------------
    # Parte 1: Cálculo do Fatorial
    # -------------------------------
    x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
    print(f'{x}! = {fatorial(x)}')

    # -------------------------------
    # Parte 2: Cadastro de Jogos
    # -------------------------------
    arquivo = 'games.txt'
    if existeArquivo(arquivo):
        print('Arquivo localizado no computador.')
    else:
        print('Arquivo inexistente.')
        criarArquivo(arquivo)

    while True:
        print('\nMENU')
        print('1 - Cadastrar novo item')
        print('2 - Listar cadastros')
        print('3 - Sair')

        op = valida_int('Escolha a opção desejada: ', 1, 3)
        if op == 1:  # Novo item
            print('\nCadastrar novo item...\n')
            nomeJogo = input('Nome do jogo: ')
            nomeVideoGame = input('Nome do videogame: ')
            cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
        elif op == 2:  # Listar
            print('\nLista de cadastros:\n')
            listarArquivo(arquivo)
        elif op == 3:  # Sair
            print('Encerrando o programa...')
            break