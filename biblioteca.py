

# PROJETO FINAL - SISTEMA DE CADASTRO DE BIBLIOTECA
# Escola de Programação Web para Meninas e Mulheres
# GRACE - ICMC/USP - 2026


import json
import os

# Lista global para armazenar os livros
livros = []

# Nome do arquivo utilizado para salvar os dados
ARQUIVO = "livros.json"



# FUNÇÃO PARA SALVAR OS LIVROS EM JSON


def salvar_livros():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)



# FUNÇÃO PARA CARREGAR OS LIVROS DO JSON


def carregar_livros():
    global livros

    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if isinstance(dados, list):
                livros = dados
            else:
                print("Arquivo JSON com formato inválido.")
                livros = []

        except (json.JSONDecodeError, OSError):
            print("Erro ao carregar os livros.")
            livros = []
    else:
        livros = []



# FUNÇÃO PARA CADASTRAR LIVROS


def cadastrar_livro():
    print("\n=== Cadastro de Livro ===")

    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    ano = input("Digite o ano de publicação: ").strip()

    # Verifica se os campos foram preenchidos
    if not titulo or not autor or not ano:
        print("Erro: todos os campos são obrigatórios.")
        return

    # Verifica se o ano é um número válido
    if not ano.isdigit() or int(ano) == 0:
        print("Erro: digite um ano válido.")
        return

    # Evita cadastrar livros repetidos
    for livro in livros:
        if (livro["titulo"].lower() == titulo.lower()
                and livro["autor"].lower() == autor.lower()):
            print("Este livro já está cadastrado.")
            return

    # Cria um dicionário com os dados do livro
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "disponivel": True
    }

    # Adiciona o livro à lista
    livros.append(livro)

    # Salva os dados no arquivo JSON
    salvar_livros()

    print("Livro cadastrado com sucesso!")



# FUNÇÃO PARA LISTAR OS LIVROS


def listar_livros():
    print("\n=== Livros Cadastrados ===")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for numero, livro in enumerate(livros, start=1):
        print("---------------------------")
        print("Livro:", numero)
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])

        if livro["disponivel"] == True:
            print("Disponibilidade: Sim")
        else:
            print("Disponibilidade: Não")

    print("---------------------------")



# FUNÇÃO PARA BUSCAR LIVROS


def buscar_livro():
    print("\n=== Buscar Livros ===")

    busca = input(
        "Digite o título ou autor do livro: "
    ).strip().lower()

    if not busca:
        print("Digite um título ou autor para pesquisar.")
        return

    encontrado = False

    for livro in livros:
        if (busca in livro["titulo"].lower()
                or busca in livro["autor"].lower()):

            print("---------------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])

            if livro["disponivel"] == True:
                print("Disponibilidade: Sim")
            else:
                print("Disponibilidade: Não")

            encontrado = True

    if encontrado == False:
        print("Nenhum livro encontrado.")



# FUNÇÃO PARA EMPRESTAR LIVROS


def emprestar_livro():
    print("\n=== Empréstimo de Livro ===")

    titulo = input(
        "Digite o título do livro: "
    ).strip().lower()

    if not titulo:
        print("Digite o título do livro.")
        return

    for livro in livros:
        if livro["titulo"].lower() == titulo:

            if livro["disponivel"] == True:
                livro["disponivel"] = False

                salvar_livros()

                print("Livro emprestado com sucesso!")
            else:
                print("Este livro já está emprestado.")

            return

    print("Livro não encontrado.")



# FUNÇÃO PARA DEVOLVER LIVROS


def devolver_livro():
    print("\n=== Devolução de Livro ===")

    titulo = input(
        "Digite o título do livro: "
    ).strip().lower()

    if not titulo:
        print("Digite o título do livro.")
        return

    for livro in livros:
        if livro["titulo"].lower() == titulo:

            if livro["disponivel"] == False:
                livro["disponivel"] = True

                salvar_livros()

                print("Livro devolvido com sucesso!")
            else:
                print("Este livro já está disponível.")

            return

    print("Livro não encontrado.")



# FUNCIONALIDADE EXTRA 1 - CONTADOR DE ACERVO


def contador_acervo():
    print("\n=== Contador de Acervo ===")

    total = len(livros)
    disponiveis = 0
    emprestados = 0

    for livro in livros:
        if livro["disponivel"] == True:
            disponiveis += 1
        else:
            emprestados += 1

    print("Total de livros:", total)
    print("Livros disponíveis:", disponiveis)
    print("Livros emprestados:", emprestados)



# FUNCIONALIDADE EXTRA 2 - ORDENAÇÃO DE LIVROS


def ordenar_livros():
    print("\n=== Ordenar Livros ===")
    print("1 - Ordem alfabética por título")
    print("2 - Ordem cronológica por ano")

    opcao = input("Escolha uma opção: ")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    if opcao == "1":
        livros_ordenados = sorted(
            livros,
            key=lambda livro: livro["titulo"].lower()
        )

    elif opcao == "2":
        livros_ordenados = sorted(
            livros,
            key=lambda livro: int(livro["ano"])
        )

    else:
        print("Opção inválida.")
        return

    print("\n=== Livros Ordenados ===")

    for livro in livros_ordenados:
        print("---------------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])

        if livro["disponivel"]:
            print("Disponibilidade: Sim")
        else:
            print("Disponibilidade: Não")



# FUNCIONALIDADE EXTRA 3 - REMOVER LIVROS


def remover_livro():
    print("\n=== Remover Livro ===")

    titulo = input(
        "Digite o título do livro que deseja remover: "
    ).strip().lower()

    if not titulo:
        print("Digite o título do livro.")
        return

    for livro in livros:
        if livro["titulo"].lower() == titulo:

            print("Livro encontrado:", livro["titulo"])
            print("Autor:", livro["autor"])

            confirmar = input(
                "Deseja realmente remover? (S/N): "
            ).strip().lower()

            if confirmar == "s":
                livros.remove(livro)

                salvar_livros()

                print("Livro removido com sucesso!")
            else:
                print("Remoção cancelada.")

            return

    print("Livro não encontrado.")


# FUNÇÃO MENU PRINCIPAL


def menu():

    # Carrega os livros salvos ao iniciar
    carregar_livros()

    while True:
        print("\n=== Sistema de Cadastro de Biblioteca ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livros")
        print("4 - Emprestar livro")
        print("5 - Devolver livro")
        print("6 - Contador de acervo")
        print("7 - Ordenar livros")
        print("8 - Remover livro")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            cadastrar_livro()

        elif opcao == "2":
            listar_livros()

        elif opcao == "3":
            buscar_livro()

        elif opcao == "4":
            emprestar_livro()

        elif opcao == "5":
            devolver_livro()

        elif opcao == "6":
            contador_acervo()

        elif opcao == "7":
            ordenar_livros()

        elif opcao == "8":
            remover_livro()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")



# INICIAR O PROGRAMA

if __name__ == "__main__":
    menu()
