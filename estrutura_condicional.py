def exercicio1_lucro_loja():
    faturamento = 1000
    custo = 500
    lucro = faturamento - custo
    print(f'O faturamento foi {faturamento}, custo {custo}, lucro {lucro} reais.')


def exercicio2_meta_iphone():
    meta = 50000
    qtde_vendida = 15368
    if qtde_vendida > meta:
        print(f'Batemos a meta! Vendemos {qtde_vendida} unidades.')
    else:
        print(f'Não batemos a meta. Vendemos {qtde_vendida} unidades de {meta}.')


def exercicio3_taxa_rendimento():
    meta = 0.05
    rendimento = 0.10
    if rendimento > meta:
        if rendimento > 0.20:
            taxa = 0.04
        else:
            taxa = 0.02
    else:
        taxa = 0
    print(f'A taxa foi de {taxa}')


def exercicio4_bonus_loja():
    meta = 20000
    vendas = 222000
    if vendas < meta:
        print('Não ganhou bônus!')
    elif vendas > (meta * 2):
        bonus = 0.07 * vendas
        print(f'Ganhou {bonus} de bônus')
    else:
        bonus = 0.03 * vendas
        print(f'Ganhou {bonus} de bônus!')


def exercicio5_bonus_funcionarios():
    vendas = [1000, 770, 2700]
    meta = 1000
    for i, v in enumerate(vendas, 1):
        if v >= 2000:
            bonus = v * 0.15
        elif v >= meta:
            bonus = v * 0.10
        else:
            bonus = 0
        print(f'O funcionário {i} ganhou {bonus} de bônus.')


def exercicio6_bonus_combinado():
    meta_funcionario = 10000
    meta_loja = 250000
    vendas_funcionario = 15000
    vendas_loja = 280000

    if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
        bonus = 0.03 * vendas_funcionario
        print(f'Funcionário recebeu {bonus} reais de bônus.')
    else:
        print('Funcionário não recebeu bônus.')


def exercicio7_avaliacao_funcionario():
    meta_funcionario = 10000
    meta_loja = 250000
    vendas_funcionario = 15000
    vendas_loja = 280000
    nota_funcionario = 5
    meta_nota = 9

    if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
        bonus = 0.03 * vendas_funcionario
        print(f'Funcionário recebeu {bonus} reais de bônus.')
    else:
        print('Funcionário não recebeu bônus.')


def exercicio8_lucro_input():
    faturamento = input('Qual foi o faturamento da loja? ')
    custo = input('Qual foi o custo da loja? ')
    if faturamento and custo:
        lucro = int(faturamento) - int(custo)
        print(f'O lucro da loja foi de {lucro} reais.')
    else:
        print('Preencha corretamente.')


def exercicio9_estoque():
    produto = input('Digite o nome do produto: ')
    categoria = input('Digite a categoria do produto: ')
    qtde = input('Digite a quantidade em estoque: ')
    if produto and categoria and qtde:
        qtde = int(qtde)
        if categoria == 'alimentos' and qtde < 50:
            print(f'Solicitar {produto}. Apenas {qtde} em estoque.')
        elif categoria == 'bebidas' and qtde < 75:
            print(f'Solicitar {produto}. Apenas {qtde} em estoque.')
        elif qtde < 30:
            print(f'Solicitar {produto}. Apenas {qtde} em estoque.')
    else:
        print('Preencha corretamente.')


def exercicio10_bissexto():
    ano = int(input('Digite o ano: '))
    if ano % 4 == 0:
        print('Pode ser bissexto.')
    else:
        print('Definitivamente não é bissexto.')


def exercicio11_triangulo():
    a = float(input('Digite o 1º lado: '))
    b = float(input('Digite o 2º lado: '))
    c = float(input('Digite o 3º lado: '))
    if (a + b > c and a + c > b and b + c > a) and (a > 0 and b > 0 and c > 0):
        if a == b == c:
            print('Triângulo equilátero')
        elif a != b and a != c and b != c:
            print('Triângulo escaleno')
        else:
            print('Triângulo isósceles')
    else:
        print('O triângulo não existe!')


def exercicio12_calculadora_simples():
    print('CALCULADORA')
    a = float(input('Digite o 1º número: '))
    b = float(input('Digite o 2º número: '))
    op = input('Qual operação (+,-,*,/)? ')
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    else:
        print('Operação inválida')


def exercicio13_calculadora_menu():
    print('------------------------------------------')
    print('CALCULADORA')
    print('+ Adição | - Subtração | * Multiplicação | / Divisão')
    print('------------------------------------------')
    op = input('Operação: ')
    a = int(input('Digite o 1º valor: '))
    b = int(input('Digite o 2º valor: '))
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    else:
        print('Encerrando...')


def exercicio14_conta_luz():
    kwh = float(input('Quantidade consumida em kWh: '))
    tipo = input('Tipo de instalação (R/I/C): ')
    if tipo == 'R':
        preco = 0.65 if kwh >= 500 else 0.40
    elif tipo == 'I':
        preco = 0.60 if kwh >= 5000 else 0.55
    elif tipo == 'C':
        preco = 0.60 if kwh >= 1000 else 0.55
    else:
        print('Instalação inválida.')
        return
    print(f'Total a pagar = R${kwh * preco:.2f}')


# ---------------- MENU PRINCIPAL ---------------- #
def main():
    print("Escolha um exercício para rodar:")
    opcoes = {
        "1": exercicio1_lucro_loja,
        "2": exercicio2_meta_iphone,
        "3": exercicio3_taxa_rendimento,
        "4": exercicio4_bonus_loja,
        "5": exercicio5_bonus_funcionarios,
        "6": exercicio6_bonus_combinado,
        "7": exercicio7_avaliacao_funcionario,
        "8": exercicio8_lucro_input,
        "9": exercicio9_estoque,
        "10": exercicio10_bissexto,
        "11": exercicio11_triangulo,
        "12": exercicio12_calculadora_simples,
        "13": exercicio13_calculadora_menu,
        "14": exercicio14_conta_luz,
    }

    for k, v in opcoes.items():
        print(f"{k} - {v.__name__}")

    escolha = input("Digite o número do exercício: ")
    if escolha in opcoes:
        opcoes[escolha]()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()