import pytest


@pytest.fixture  # Criamos a fixture por meio do decorador pytest.fixture
def my_list():  # Por padrão, o nome da fixture será o nome da função
    return [1, 2, 3]  # Retorna o valor que a fixture possuirá


def test_a_simple_test():
    assert True


def test_sum(my_list):  # Recebemos a fixture como parâmetro da função de teste
    assert sum(my_list) == 6  # Usamos a lista retornada pela fixture


def test_list_item_multiply(my_list):  # Recebemos a mesma fixture aqui também
    assert [item * 3 for item in my_list] == [3, 6, 9]


# capsys


def test_print_to_stdout(capsys):
    print("Hello, world!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"  # print coloca \n automaticamente


def test_error_to_stderr(capsys):
    import sys

    sys.stderr.write("Error message\n")
    captured = capsys.readouterr()
    assert captured.err == "Error message\n"


# monkeypatch


def my_function():
    return f"Você digitou {input('Digite algo: ')}!"


def test_my_function(monkeypatch):
    # Input recebe um parâmetro que mock_input não usa, por isso o _
    def mock_input(_):
        return "Python"

    # Trocamos a input do sistema pela nossa mock_input
    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "Você digitou Python!"
