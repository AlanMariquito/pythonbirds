class Pessoa:
    def __init__(self, nome=None, idade=37):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa('Batata')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Alan"
    print(p.nome)
    print(p.idade)
