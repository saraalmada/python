def basicos():
    email = 'sara@gmail.com'
    nome = 'Sara de Almada Torres'

    print('Tamanho de e-mail ' + str(len(email)) + ' caracteres')
    print('Primeiro caractere ' + str(nome[0]))
    print('Último caractere ' + str(nome[-1]))
    print('Servidor do email ' + email[5:10])


def validar_cpf():
    cpf = input('Insira o CPF (digite apenas números): ')
    cpf = cpf.strip().replace('.', '').replace('-', '')

    if len(cpf) == 11 and cpf.isnumeric():
        print(f'CPF válido: {cpf}')
    else:
        print('Digite seu CPF corretamente e digite apenas números')


def validar_email():
    nome = input('Digite seu nome: ')
    email = input('Digite o seu email: ')

    if nome and email:
        pos_a = email.find('@')
        servidor = email[pos_a:]
        if pos_a != -1 and '.' in servidor:
            print('Cadastro concluído')
        else:
            print('Email inválido')
    else:
        print('Digite o seu nome e e-mail corretamente')


def formatacao_numeros():
    custo = 5000
    faturamento = 2700
    lucro = faturamento - custo

    print(f'Faturamento foi {faturamento:+,} e lucro foi {lucro:+,}')
    print(f'Faturamento foi {faturamento:.2f} e lucro foi {lucro:.1f}')

    custo = 500
    faturamento = 1300
    lucro = faturamento - custo
    print(f'Margem de lucro foi de {lucro:.1%}')

    custo = 5000
    faturamento = 27000
    lucro = faturamento - custo
    print(f'Faturamento foi R${faturamento:,.2f} e lucro foi R${lucro:,.2f}')

    lucro_texto = f'R${lucro:_.2f}'
    print(lucro_texto.replace('.', ',').replace('_', '.'))

    imposto = 0.15758
    preco = 100
    valor_imposto = round(preco * imposto, 1)
    print(f'Imposto sobre o preço é de {valor_imposto}')


def operacoes_strings():
    texto = 'sara'
    print(texto.capitalize())

    texto = 'Sara'
    print(texto.casefold())

    texto = 'sara@gmail.com'
    print(texto.count('a'))
    print(texto.endswith('gmail.com'))
    print(texto.find('@'))

    texto = 'João123'
    print(texto.isalnum())
    print(texto.isalpha())

    texto = '123'
    print(texto.isnumeric())

    texto = '1000.00'
    print(texto.replace('.', ','))

    texto = 'sara@gmail.com'
    print(texto.split('@'))

    texto = '''Olá, bom dia
Venho te dar boas vindas!
Adeus
'''
    print(texto.splitlines())

    texto = 'BEB123456'
    print(texto.startswith('BEB'))

    texto = ' BEB123456 '
    print(texto.strip())

    texto = 'sara de almada'
    print(texto.title())

    texto = 'beb12345'
    print(texto.upper())


def desconto_produto():
    preco_inicial = float(input('Qual o preço do produto? '))
    percentual = float(input('Qual desconto em % deseja aplicar ao produto? '))

    desconto = percentual / 100 * preco_inicial
    preco_final = preco_inicial - desconto

    print(f'O desconto será de R${desconto:.2f} e o preço final do produto será R${preco_final:.2f}')


def aluguel_carros():
    km = int(input('Quantos km foram percorridos? '))
    dias = int(input('Em quantos dias? '))

    preco = 60 * dias + (0.15 * km)
    print(f'Visto que foram percorridos {km}km em {dias} dias. O valor a pagar será de R${preco:.2f}.')


def frase_metade():
    frase = input('Digite uma frase: ')
    tam = len(frase)

    frase2 = frase[:int(tam / 2)]
    print(frase2[-2:])


# ==================================
# Execução dos exercícios
# (descomente a função que deseja testar)
# ==================================

# basicos()
# validar_cpf()
# validar_email()
# formatacao_numeros()
# operacoes_strings()
# desconto_produto()
# aluguel_carros()
# frase_metade()