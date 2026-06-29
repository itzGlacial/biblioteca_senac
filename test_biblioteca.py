import biblioteca as b

def test_adicionar_livro():
    b.livros.clear()
    b.adicionar_livro("1984", "George Orwell")
    assert len(b.livros) == 1
    assert b.livros[0]["titulo"] == "1984"


def test_registrar_usuario():
    b.usuarios.clear()
    b.registrar_usuario("João")
    assert len(b.usuarios) == 1
    assert b.usuarios[0]["nome"] == "João"


def test_emprestar_livro():
    b.livros.clear()
    b.usuarios.clear()

    b.adicionar_livro("Duna", "Frank Herbert")
    b.registrar_usuario("Maria")

    b.emprestar_livro("Maria", "Duna")

    assert b.livros[0]["disponivel"] is False
    assert "Duna" in b.usuarios[0]["livros_emprestados"]