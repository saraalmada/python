# ==================================================
# PRÁTICA COM LISTAS
# ==================================================

# Lista de produtos e produção
produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for i in range(len(produtos)):
    print(f'{producao[i]} unidades produzidas de {produtos[i]}')

print("\n--- Percorrendo lista de produtos ---")
for produto in produtos:
    print(produto)

print("\n--- Percorrendo string como lista de caracteres ---")
texto = 'sara@gmail.com'
for ch in texto:
    print(ch)

# Lista de funcionários
funcionarios = [
    'Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz',
    'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisco', 'Ana', 'João',
    'Mariana', 'Pedro', 'Sofia', 'Gabriel', 'Laura', 'Rafael', 'Beatriz', 'Lucas'
]
print("\n--- Funcionários enumerados ---")
for i, funcionario in enumerate(funcionarios):
    print(f'{i}. {funcionario}')