class livro ():
    paginas = 5

    def __init__(self, titulo, autor, argumentos):  # Construtor
        pass

    def __str__(self):  # sempre que você fizer print(livro) será chamada essa função String
        pass

    def __len__(self):  # Sempre que você fizer  len(livro) será chamada essa função len
        return self.paginas


    #E existem vários outros métodos especiais (PESQUISAR)