# SISTEMA DE BIBLIOTECA
# =========================

livros = []
usuarios = []


# LIVROS
# -------------------------
def adicionar_livro(titulo, autor):
    livros.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })
    print("Livro adicionado com sucesso!")


def remover_livro(titulo):
    global livros
    livros = [livro for livro in livros if livro["titulo"] != titulo]
    print("Livro removido (se existia).")


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'{livro["titulo"]} - {livro["autor"]} [{status}]')


# USUÁRIOS
# -------------------------
def registrar_usuario(nome):
    usuarios.append({
        "nome": nome,
        "livros_emprestados": []
    })
    print("Usuário registrado com sucesso!")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f'Nome: {usuario["nome"]} | Livros: {usuario["livros_emprestados"]}')


# EMPRÉSTIMOS
# -------------------------
def emprestar_livro(nome_usuario, titulo_livro):
    usuario = next((u for u in usuarios if u["nome"] == nome_usuario), None)
    livro = next((l for l in livros if l["titulo"] == titulo_livro), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    if not livro:
        print("Livro não encontrado.")
        return

    if not livro["disponivel"]:
        print("Livro já emprestado.")
        return

    livro["disponivel"] = False
    usuario["livros_emprestados"].append(titulo_livro)
    print("Empréstimo realizado com sucesso!")


def livros_emprestados():
    print("=== LIVROS EMPRESTADOS ===")
    for livro in livros:
        if not livro["disponivel"]:
            print(livro["titulo"])


# MENU
# -------------------------
def menu():
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1 - Adicionar livro")
        print("2 - Remover livro")
        print("3 - Listar livros")
        print("4 - Registrar usuário")
        print("5 - Listar usuários")
        print("6 - Emprestar livro")
        print("7 - Livros emprestados")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha: "))

            if opcao == 1:
                t = input("Título: ")
                a = input("Autor: ")
                adicionar_livro(t, a)

            elif opcao == 2:
                t = input("Título: ")
                remover_livro(t)

            elif opcao == 3:
                listar_livros()

            elif opcao == 4:
                n = input("Nome do usuário: ")
                registrar_usuario(n)

            elif opcao == 5:
                listar_usuarios()

            elif opcao == 6:
                n = input("Nome do usuário: ")
                t = input("Título do livro: ")
                emprestar_livro(n, t)

            elif opcao == 7:
                livros_emprestados()

            elif opcao == 0:
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite um número válido.")

if __name__ == "__main__":
    menu()
