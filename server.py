import Pyro4
import time
import os


@Pyro4.expose
class Aviao:
    def __init__(self, nome):
        """Definição dos valores iniciais no construtor e pah """
        self.posicaoAtual = 0
        self.nome = nome
        self.localizacao_atual = "Rio Grande do Norte"
        self.localizacoes = ["Rio Grande do Norte",
                             "Bahia", "São Paulo", "Acre"]
        self.origem = 0

    def draw_way(self):
        os.system('cls')
        a = self.posicaoDestino-self.origem
        if (a >= 1):

            print(self.localizacao_atual, end=" ")
            for i in range(self.origem, a+1):
                if (i == self.posicaoAtual):
                    print("✈", end=" ")
                else:
                    print("---", end=" ")

            print(self.localizacoes[self.posicaoDestino], end=" ")
        else:

            print(self.localizacao_atual, end=" ")
            for i in range(self.origem+1, self.posicaoDestino, -1):
                if (i == self.posicaoAtual):
                    print("✈", end=" ")
                else:
                    print("---", end=" ")

            print(self.localizacoes[self.posicaoDestino], end=" ")

    def irAteDestino(self, destino):
        self.posicaoAtual = self.origem
        self.posicaoDestino = destino-1

        if(self.posicaoAtual != self.posicaoDestino):
            while True:
                if self.posicaoAtual < self.posicaoDestino:
                    self.posicaoAtual += 1
                    self.draw_way()
                elif self.posicaoAtual > self.posicaoDestino:
                    self.draw_way()
                    self.posicaoAtual -= 1
                elif self.posicaoAtual == self.posicaoDestino:
                    4
                    self.origem = destino-1
                    self.localizacao_atual = self.localizacoes[destino-1]
                    print("O avião chegou ao seu destino")
                    return "O avião chegou ao seu destino"
                time.sleep(1)
        else:
            print("Você já se encontra no seu destino")
            return "Você já se encontra no seu destino"

    def getPosicao(self):
        return self.posicaoAtual

    def getLocalizacao(self):
        return self.localizacao_atual


daemon = Pyro4.Daemon()
aviao = Aviao(nome='AEROBUS-2020.1')
uri = daemon.register(aviao)
ns = Pyro4.locateNS()
ns.register('obj', uri)

print(uri)
daemon.requestLoop()
