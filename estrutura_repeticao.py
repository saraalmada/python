def exercicio1_producao():
    produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
    producao = [15000, 12000, 13000, 5000, 250]
    for i in range(len(produtos)):
        print(f'{producao[i]} unidades produzidas de {produtos[i]}')


def exercicio2_for_texto():
    produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
    texto = 'sara@gmail.com'

    for produto in produtos:
        print(produto)

    for ch in texto:
        print(ch)


def exercicio3_vendas_meta():
    vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70,
              90, 80, 1100, 999, 900, 880, 50, 1111, 120, 300, 450, 800]
    meta = 1000
    c = 0
    for vendedor in vendas:
        if vendedor >= meta:
            c += 1
            print(vendedor)
    porcentagem = (c / len(vendas)) * 100
    print(f'\n{porcentagem:.1f}% dos funcionários bateram a meta')


def exercicio4_enumerate_funcionarios():
    funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco',
                    'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel',
                    'Pedro', 'Francisco', 'Ana', 'João', 'Mariana',
                    'Pedro', 'Sofia', 'Gabriel', 'Laura', 'Rafael',
                    'Beatriz', 'Lucas']
    for i, funcionario in enumerate(funcionarios):
        print(f'{i}. {funcionario}')


def exercicio5_estoque_minimo():
    estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70,
               90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
    produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua',
                'del valle', 'dolly', 'red bull', 'cachaça', 'vinho',
                'suco de laranja', 'refrigerante de limão', 'leite',
                'cerveja pilsen', 'vodka', 'energético', 'água tônica',
                'whisky', 'chá gelado', 'espumante', 'suco de uva', 'cerveja IPA']
    nivel_minimo = 50

    for i, qtde in enumerate(estoque):
        if qtde < nivel_minimo:
            print(produtos[i], qtde)


def exercicio6_crescimento_vendas():
    produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle',
                'geladeira', 'adega', 'notebook dell', 'notebook hp',
                'microsoft surface', 'webcam', 'caixa de som', 'microfone',
                'câmera canon', 'sara']
    vendas2019 = [558147, 712358, 573823, 405252, 718654, 531580, 973139,
                  892292, 422760, 154753, 887061, 438508, 237467, 489705,
                  328311, 591128]
    vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331,
                  546816, 694913, 539704, 324831, 667179, 295633, 725316,
                  544622, 994383]

    for i, produto in enumerate(produtos):
        if vendas2020[i] > vendas2019[i]:
            crescimento = vendas2020[i] / vendas2019[i] - 1
            print(f'{produto}: R${vendas2019[i]:,} em 2019, '
                  f'R${vendas2020[i]:,} em 2020 '
                  f'({crescimento:.1%} de crescimento)')


def exercicio7_fabricas_estoque():
    estoque = [
        [294, 125, 269, 208, 783, 852, 259, 371, 47, 182, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
        [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
        [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
        [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
        [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 65]
    ]
    fabricas = ['Sara Manufacturing', 'Fábrica Nestlé', 'Python Manufaturas',
                'Produções e Cia', 'Manufatura e Cia']
    nivel_minimo = 50

    fabricas_abaixo = []
    for i, lista in enumerate(estoque):
        for qtde in lista:
            if qtde < nivel_minimo and fabricas[i] not in fabricas_abaixo:
                fabricas_abaixo.append(fabricas[i])
    print(fabricas_abaixo)


def exercicio8_vendas_meta_bugado():
    # Exemplo de código com bug corrigido
    vendas = [
        ['João', 15000],
        ['Julia', 27000],
        ['Marcus', 9900],
        ['Maria', 3750],
        ['Ana', 10300],
        ['Alon', 7870],
    ]
    meta = 10000
    c = 0
    for nome, venda in vendas:
        if venda >= meta:
            c += 1
    porcentagem = c / len(vendas)
    print(f'{porcentagem:.0%} bateram a meta')


def exercicio9_vendas_meta_lista():
    vendas = [
        ['João', 15000],
        ['Julia', 27000],
        ['Marcus', 9900],
        ['Maria', 3750],
        ['Ana', 10300],
        ['Alon', 7870],
    ]
    meta = 10000
    bateram_meta = []

    for venda in vendas:
        if venda[1] >= meta:
            bateram_meta.append(venda)

    print(bateram_meta)
    porc = len(bateram_meta) / len(vendas)
    print(f'{porc:.0%} bateram a meta')


# ---------------- MENU PRINCIPAL ---------------- #
def main():
    print("Escolha um exercício de listas/loops para rodar:")
    opcoes = {
        "1": exercicio1_producao,
        "2": exercicio2_for_texto,
        "3": exercicio3_vendas_meta,
        "4": exercicio4_enumerate_funcionarios,
        "5": exercicio5_estoque_minimo,
        "6": exercicio6_crescimento_vendas,
        "7": exercicio7_fabricas_estoque,
        "8": exercicio8_vendas_meta_bugado,
        "9": exercicio9_vendas_meta_lista,
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