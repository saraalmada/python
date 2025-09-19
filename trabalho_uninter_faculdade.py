# QUESTÃO 1

print('SEJA BEM-VINDO(A) a Loja da Sara Almada.')
print('----------------------------------------')

valor_unitario = float(input('Digite o valor do produto: R$'))
qtd = int(input('Digite a quantidade desejada: '))

# CÁLCULO DO VALOR TOTAL SEM DESCONTO
total_sem_desconto = valor_unitario * qtd

# CÁLCULO DAS PORCENTAGENS DE DESCONTO
if total_sem_desconto < 2500:
    desconto = 0 # SEM DESCONTO
elif total_sem_desconto >= 2500 and total_sem_desconto < 6000:
    desconto = 0.04 # 4% DE DESCONTO
elif total_sem_desconto >= 6000 and total_sem_desconto < 10000:
    desconto = 0.07 # 7% DE DESCONTO
else:
    desconto = 0.11 # 11% DE DESCONTO

#CÁLCULO DO VALOR TOTAL COM DESCONTO
total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)

print('--------------------------------------------------')
print('Resumo do pedido: ')
(print(f'O valor SEM desconto: R${total_sem_desconto:.2f}'))
(print(f'O valor COM desconto: R${total_com_desconto:.2f}'))



# QUESTÃO 2

print('SEJA BEM-VINDO(A) a Loja de Gelados da Sara Almada.')
print('---------------------------Cardápio--------------------------')
print('-------------------------------------------------------------')
print('------|   Tamanho   |   Cupuaçu (CP)   |   Açaí (AC)   |-----')
print('------|      P      |      R$ 9.00     |   R$ 11.00    |-----')
print('------|      M      |     R$ 14.00     |   R$ 16.00    |-----')
print('------|      G      |     R$ 18.00     |   R$ 20.00    |-----')
print('-------------------------------------------------------------')

# VARIÁVEL ACUMULADORA
total_pedido = 0

while True:
    
    # Verificação se o usuário entrar com valor diferente de CP e AC
    sabor = input('Digite o sabor desejado (CP/AC): ').upper()
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido. Tente novamente\n')
        continue # VOLTA AO INÍCIO DO PROGRAMA
        
    # Verificação se o usuário entrar com valor diferente de P, M ou G
    tamanho = input('Digite o tamanho desejado (P/M/G): ').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente\n')
        continue # VOLTA AO INÍCIO DO PROGRAMA
        
    # Preço de acordo com o sabor e tamanho escolhidos
    if sabor == 'CP':
        nome_sabor = 'Cupuaçu'
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        elif tamanho == 'G':
            preco = 18
    if sabor == 'AC':
        nome_sabor = 'Açaí'
        if tamanho == 'P':
            preco = 11
        if tamanho == 'M':
            preco = 16
        if tamanho == 'G':
            preco = 20

    print(f'Você pediu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n') # Especificação do gelato selecionado

    total_pedido += preco # Variável acumuladora somando os valores dos pedidos

    continuar = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if continuar != 'S':
        break # ENCERRA O LOOP

print(f'\nO valor total a ser pago: R$ {total_pedido:.2f}')



# QUESTÃO 3

print('SEJA BEM-VINDO(A) a Copiadora da Sara Almada')

# FUNÇÕES
def escolha_servico():
    while True:
        print('\nDigite o tipo de serviço desejado: ')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('').upper()
        if servico == 'DIG': # Digitalização
            return 1.10
        elif servico == 'ICO': # Impressão Colorida
            return 1.00
        elif servico == 'IPB': # Impressão Preto e Branco
            return 0.40
        elif servico == 'FOT': # Fotocópia
            return 0.20
        else:
            print('Escolha inválida, digite o tipo de serviço novamente')

def num_pagina():
    while True:
        try:
            paginas = int(input('\nDigite o número de páginas: '))
            if paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez. Por favor, entre com o número de páginas novamente.')
            elif paginas >= 2000:
                return paginas * 0.75 # 25% de desconto
            elif paginas >= 200:
                return paginas * 0.80 # 20% de desconto
            elif paginas >= 20:
                return paginas * 0.85 # 15% de desconto
            elif paginas > 0:
                return paginas # Sem desconto
            else:
                print('Número de páginas deve ser maior que zero.')
        except ValueError: # VERIFICAÇÃO CASO O QUE FOR DIGITADO PELO USUÁRIO FOR DIFERENTE DE UM NÚMERO INTEIRO
            print('Entrada inválida. Digite um número inteiro')

def servico_extra():
    while True:
        print('\nDeseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15,00')
        print('2 - Encadernação Capa Dura - R$ 40,00')
        print('0 - Não desejo mais nada')
        extra = input('')
        if extra == '1': # SIMPLES
            return 15.00
        elif extra == '2': # CAPA DURA
            return 40.00
        elif extra == '0': # NADA
            return 0.00
        else:
            print('Opção inválida. Digite 1, 2 ou 0')

# PROGRAMA PRINCIPAL
try:
    servico = escolha_servico()
    num_pagina = num_pagina()
    extra = servico_extra()

    # Cálculo do valor final da conta
    total = (servico * num_pagina) + extra

    print(f'\nTotal: R$ {total:.2f} (serviço: R$ {servico:.2f} * páginas: {num_pagina} + extra: R$ {extra:.2f})')
    
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')


print('SEJA BEM-VINDO(A) a Livraria da Sara Almada')

# Implentação da lista vazia e da variável
lista_livro = []
id_global = 0



# QUESTÃO 4

# FUNÇÕES
def cadastrar_livro(id):
    print('\n-----------------------------------------')
    print('---------- MENU CADASTRAR LIVRO -----------')
    input(f'Id do livro: ')
    nome = input('Por favor, digite o nome do livro: ')
    autor = input('Por favor, digite o autor do livro: ')
    editora = input('Por favor, digite a editora do livro: ')
    livro = {     # DICIONÁRIO
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    # CÓPIA PARA LISTA
    lista_livro.append(livro)


def consultar_livro():
    while True:
        print('-------------------------------------------')
        print('---------- MENU CONSULTAR LIVRO -----------')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por autor')
        print('4 - Retornar ao menu')
        opcao = input('')

        if opcao == '1': # CONSULTAR TODOS
            for livro in lista_livro: 
                print(f"\nID: {livro['id']} \nNome: {livro['nome']} \nAutor: {livro['autor']} \nEditora: {livro['editora']}")
        elif opcao == '2': # CONSULTAR POR ID
            try:
                id_busca = int(input('Digite o ID do livro: '))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_busca:
                        print(f"\nID: {livro['id']} \nNome: {livro['nome']} \nAutor: {livro['autor']} \nEditora: {livro['editora']}")
                        encontrado = True
                if not encontrado:
                    print('ID não encontrado.')
            except ValueError:
                print('Entrada inválida. Digite um número inteiro')
        elif opcao == '3': # CONSULTAR POR AUTOR
            autor_busca = input('Digite o nome do autor: ')
            encontrados = [livro for livro in lista_livro if livro['autor'].lower() == autor_busca.lower()]
            if encontrados:
                print(f'\nLivros do autor "{autor_busca}":')
                for livro in encontrados:
                    print(f"\nID: {livro['id']} \nNome: {livro['nome']} \nAutor: {livro['autor']} \nEditora: {livro['editora']}")
            else:
                print('Nenhum livro encontrado para este autor.')
        elif opcao == '4': # FINALIZA LOOP
            break
        else: # VOLTA AO INÍCIO DO LOOP
            print('Opção inválida. Tente novamente')


def remover_livro():
    while True:
        try:
            id_remover = int(input('Digite o ID do livro que deseja remover: '))
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print('Livro removido com sucesso!')
                    return
            print('ID inválido. Tente novamente')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro')


# PROGRAMA PRINCIPAL
while True:
    print('-------------------------------------------')
    print('\n------------ MENU PRINCIPAL -------------')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Encerrar Programa')
    opcao = input('')

    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4': # FINALIZA O PROGRAMA
        break
    else: # VOLTA AO INÍCIO DO LOOP
        print('Opção inválida. Tente novamente')