'''
Crie uma classe animal com atributos e métodos, posteriormente, crie uma classe que herde seus atributos, e possuía os seus atributos próprios. 

Crie dois objetos da classe filha.
'''

class Animal():
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def exibir_info(self):
        print(f"Nome: {self.nome} \nEspécie: {self.especie}")

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.raca = raca

    def exibir_info(self):
        super().exibir_info()
        print(f"Raça: {self.raca}")

    def fazer_som(self):
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def __init__(self, nome, especie, cor):
        super().__init__(nome, especie)
        self.cor = cor

    def exibir_info(self):
        super().exibir_info()
        print(f"Cor: {self.cor}")

    def fazer_som(self):
        print("O gato faz: Miau!")

cachorro = Cachorro("Rex", "Canis lupus familiaris", "Labrador")
gato = Gato("Akira", "Felis catus", "Laranja")

cachorro.exibir_info()
cachorro.fazer_som()
print("-------------------------------")
gato.exibir_info()
gato.fazer_som()



'''
Crie um módulo onde seja possível, imprimir um texto de trás para frente. Oriente o usuário do seu uso.
'''

import reverso as rev

rev.reverso("Hello, World!")