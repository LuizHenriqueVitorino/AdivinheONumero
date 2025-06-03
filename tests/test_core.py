import pytest
from app.core import JogoAdivinhacao

@pytest.fixture
def jogo():
    return JogoAdivinhacao(minimo=1, maximo=10, max_tentativas=5)

def test_jogo_inicia_corretamente(jogo):
    assert jogo.minimo == 1
    assert jogo.maximo == 10
    assert jogo.max_tentativas == 5
    assert 1 <= jogo.numero_secreto <= 10
    assert jogo.tentativas == 0

def test_palpite_menor_que_secreto(jogo):
    jogo.numero_secreto = 5
    resposta = jogo.verificar_palpite(1)
    assert resposta == "baixo"
    assert jogo.tentativas == 1

def test_palpite_maior_que_secreto(jogo):
    jogo.numero_secreto = 5
    resposta = jogo.verificar_palpite(10)
    assert resposta == "alto"
    assert jogo.tentativas == 1

def test_palpite_igual_ao_secreto(jogo):
    jogo.numero_secreto = 5
    resposta = jogo.verificar_palpite(5)
    assert resposta == "correto"
    assert jogo.tentativas == 1

def test_incrementa_tentativas(jogo):
    jogo.numero_secreto = 5
    jogo.verificar_palpite(3)
    jogo.verificar_palpite(4)
    jogo.verificar_palpite(5)
    assert jogo.tentativas == 3

def test_poucas_tentativas_restantes(jogo):
    jogo.numero_secreto = 5
    jogo.verificar_palpite(1)
    jogo.verificar_palpite(2)
    jogo.verificar_palpite(7)
    tentativas_restantes = jogo.tentativas_restantes()
    assert jogo.tentativas == 3
    assert tentativas_restantes == 2

def test_muitas_tentativas_restantes(jogo):
    jogo.numero_secreto = 5
    jogo.verificar_palpite(1)
    tentativas_restantes = jogo.tentativas_restantes()
    assert jogo.tentativas == 1
    assert tentativas_restantes == 4

def test_perder_por_maximo_de_tentativas(jogo):
    jogo.numero_secreto = 5
    jogo.verificar_palpite(1)
    jogo.verificar_palpite(2)
    jogo.verificar_palpite(3)
    jogo.verificar_palpite(4)
    jogo.verificar_palpite(6)

    tentativas = jogo.tentativas
    tentativas_restantes = jogo.tentativas_restantes()
    acabou = jogo.jogo_acabou()

    assert tentativas == 5
    assert tentativas_restantes == 0
    assert acabou == True

