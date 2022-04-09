class Pessoa:
    nome = ''
    titulo = ''
    genero = ''
    data_nascimento = ''

    # construtor:
    def __init__(self, nome, titulo, genero, data_nascimento):
        self.nome = nome
        self.titulo = titulo
        self.genero = genero
        self.data_nascimento = data_nascimento


# Instanciando Obj :
mae = Pessoa()
pai = Pessoa()
usuario = Pessoa("jaime", "asa", "masculinio", "17/03/2000")

# Acessando Atributos =>
usuario.nome = input('Digite o nome do usuário do serviço: ')
mae.nome = input('Digite agora o nome da mãe do usuário do serviço: ')

# Outros métodos ->
# Existem outros métodos especiais e um dos mais importantes é o __str__(), que deve construir e retornar uma string,
#  representando o estado do objeto que a chamou, como no trecho a seguir:


class Livro:
    def __str__(self):
        return 'Título: {}; Estoque: {}; Preço: R${}'.format(self.titulo, self.copias_em_estoque, self.preco)

# Existem diversos outros métodos que o interpretador Python conhece e que você pode implementar para que esses comportamentos
# padrões possam também ser inseridos nas classes implementadas. Como exemplo, você pode citar o método __eq__(), que compara
# dois objetos e verifica se são iguais; ou o método __repr__(), que cria uma representação para um dado objeto; ou, por último,
#  o método __hash__(), que constrói um valor de hash utilizando o objeto que a chamou.
