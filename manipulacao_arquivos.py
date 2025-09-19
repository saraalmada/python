# ==================================================
# PRÁTICA COM ARQUIVOS
# ==================================================

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo.')
    else:
        a.write(f'{nomeJogo};{nomeVideoGame}\n')
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()


if __name__ == "__main__":
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
        if op == 1:
            nomeJogo = input('Nome do jogo: ')
            nomeVideoGame = input('Nome do videogame: ')
            cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)
        elif op == 2:
            listarArquivo(arquivo)
        elif op == 3:
            print('Encerrando o programa...')
            break