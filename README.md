# Sistema de Cadastro de Biblioteca

**Projeto Final — Escola de Programação Web para Meninas e Mulheres 2026**

**GRACE — ICMC/USP**

## Sobre o projeto

Este projeto foi desenvolvido em Python com o objetivo de criar um sistema simples de gerenciamento de biblioteca.

O programa permite cadastrar livros, consultar o acervo, realizar empréstimos e devoluções, além de organizar e controlar os livros disponíveis.

Durante o desenvolvimento, foram utilizados conceitos de programação aprendidos no curso, como funções, listas, dicionários, estruturas condicionais, laços de repetição e manipulação de arquivos.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Cadastrar livros:** permite registrar título, autor e ano de publicação.
2. **Listar livros:** exibe todos os livros cadastrados e sua disponibilidade.
3. **Buscar livros:** permite pesquisar por título ou autor.
4. **Emprestar livros:** altera a disponibilidade do livro para emprestado.
5. **Devolver livros:** registra a devolução e torna o livro disponível novamente.
6. **Contador de acervo:** mostra a quantidade total de livros, disponíveis e emprestados.
7. **Ordenar livros:** organiza o acervo por título ou ano de publicação.
8. **Remover livros:** permite excluir um livro cadastrado mediante confirmação.

## Armazenamento dos dados

Os dados são armazenados no arquivo `livros.json`.

O sistema salva automaticamente as alterações realizadas nos cadastros, empréstimos, devoluções e remoções.

Dessa forma, os livros permanecem registrados mesmo depois que o programa é encerrado.

## Tecnologias utilizadas

- Python 3
- JSON
- Visual Studio Code
- GitHub

## Como executar o projeto

1. Baixe os arquivos do repositório.
2. Mantenha `biblioteca.py` e `livros.json` na mesma pasta.
3. Abra a pasta no Visual Studio Code.
4. Abra o terminal e execute:

   `py biblioteca.py`

   Em sistemas nos quais o comando `py` não está disponível, utilize `python biblioteca.py`.

5. Escolha uma das opções do menu para utilizar o sistema.

## Estrutura do projeto

```text
Projeto_Biblioteca_Python/
│
├── biblioteca.py
├── livros.json
└── README.md
```

## Conceitos aplicados

Durante o desenvolvimento, foram trabalhados:

- Variáveis e tipos de dados
- Listas e dicionários
- Funções
- Estruturas condicionais
- Laços de repetição
- Entrada e saída de dados
- Validação de informações
- Leitura e escrita de arquivos JSON

## Autoria

**Karoline Gonçalves Ferraz de Campos**

Projeto desenvolvido como atividade final da Escola de Programação Web para Meninas e Mulheres 2026 — GRACE ICMC/USP.
