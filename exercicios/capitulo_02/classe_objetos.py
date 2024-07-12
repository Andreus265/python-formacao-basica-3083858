class dog:
    def __init__(self, nome='rex'):
        self.nome = nome
        self.cor = 'preto'
        self.patas = 4

    def som(self):
        print(self.nome + ' está latindo')

meu_cachorro = dog()
cachorro_vizinho = dog()
cachorro_bairro = dog('goku')

cachorro_bairro.som()
cachorro_vizinho.som()
meu_cachorro.som()
