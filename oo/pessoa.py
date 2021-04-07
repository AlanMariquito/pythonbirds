class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    alan = Pessoa(nome='Alan')
    batata = Pessoa(alan, nome= 'Batata')
    print(Pessoa.cumprimentar(batata))
    print(id(batata))
    print(batata.cumprimentar())
    print(batata.nome)
    print(batata.idade)
    for filho in batata.filhos:
        print(filho.nome)
    print(batata.filhos)
