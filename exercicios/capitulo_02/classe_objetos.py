class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

# Instanciando a classe
meu_cachorro = Cachorro("Rex", 5, "Labrador")

# Chamando o método latir()
meu_cachorro.latir()