# Meta de vendas
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80,
          1100, 999, 900, 880, 50, 1111, 120, 300, 450, 800]
meta = 1000

print("--- Vendedores que bateram a meta ---")
c = 0
for valor in vendas:
    if valor >= meta:
        c += 1
        print(valor)

porcentagem = (c / len(vendas)) * 100
print(f'\n{porcentagem:.1f}% dos funcionários bateram a meta')

# Estoque abaixo do nível mínimo
estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80,
           1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle',
            'dolly', 'red bull', 'cachaça', 'vinho', 'suco de laranja',
            'refrigerante de limão', 'leite', 'cerveja pilsen', 'vodka',
            'energético', 'água tônica', 'whisky', 'chá gelado',
            'espumante', 'suco de uva', 'cerveja IPA']
nivel_minimo = 50

print("\n--- Produtos abaixo do nível mínimo ---")
for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(produtos[i], qtde)

# Crescimento de vendas
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

print("\n--- Produtos que cresceram em 2020 ---")
for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print(f'{produto}: R${vendas2019[i]:,} em 2019, R${vendas2020[i]:,} '
              f'com crescimento de {crescimento:.1%}')
