from random import randint


class JogoAdivinhacao:
    def __init__(self, minimo=1, maximo=100, max_tentativas=10):
        self.minimo = minimo
        self.maximo = maximo
        self.max_tentativas = max_tentativas
        self.reiniciar()

    def reiniciar(self):
        self.numero_secreto = randint(self.minimo, self.maximo)
        self.tentativas = 0

    def verificar_palpite(self, palpite):
        self.tentativas += 1
        if palpite < self.numero_secreto:
            return "baixo"
        elif palpite > self.numero_secreto:
            return "alto"
        else:
            return "correto"

    def tentativas_restantes(self):
        return self.max_tentativas - self.tentativas

    def jogo_acabou(self):
        return self.tentativas >= self.max_tentativas
