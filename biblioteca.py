import matplotlib.pyplot as plt

livros = []


# Criando a classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade


# Cadastro de livros
def cadastrar_livro():
    titulo = input("Nome do livro: ")
    autor = input("Nome do autor: ")
    genero = input("Gênero do livro: ")
    quantidade = int(input("Informe a quantidade disponível: "))

    novo_livro = Livro(titulo, autor, genero, quantidade)

    livros.append(novo_livro)

    print("Livro cadastrado com sucesso!")


# Listar livros
def listar_livros():

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print("-=-" * 5)
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Gênero: {livro.genero}")
        print(f"Quantidade: {livro.quantidade}")


# Buscar livro pelo título
def buscar_livro():
    titulo_buscar = input("Digite o título do livro: ")

    for livro in livros:

        if livro.titulo.lower() == titulo_buscar.lower():
            print("LIVRO ENCONTRADO!")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Gênero: {livro.genero}")
            print(f"Quantidade: {livro.quantidade}")
            return

    print("Livro não encontrado.")


# Gerar gráfico
def gerar_grafico():
    generos = {}

    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de livros")
    plt.title("Quantidade de livros por gênero")
    plt.show()


# Menu principal
while True:
    print("\n--- SISTEMA DA BIBLIOTECA ---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro pelo título")
    print("4 - Gerar gráfico")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        buscar_livro()

    elif opcao == "4":
        gerar_grafico()

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")