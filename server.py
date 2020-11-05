import Pyro4
import time
import aviao

@Pyro4.expose

class Aviao:
    def __init__(self, nome):
        self.posicaoAtual = 0
        self.nome = nome

    def irAteDestino(self, posicaoDestino):
        distancia = abs(self.posicaoAtual - posicaoDestino)
        while True:
            if self.posicaoAtual < posicaoDestino:
                self.posicaoAtual++
                print(self.posicaoAtual)
            elif self.posicaoAtual > posicaoDestino:
                self.posicaoAtual--
                print(self.posicaoAtual)
            elif self.posicaoAtual = posicaoDestino:
                return "O avião chegou ao seu destino"
            time.sleep(1)


daemon = Pyro4.Daemon()
uri = daemon.register(Aviao)
ns = Pyro4.locateNS()
ns.register('obj', uri)

print(uri)
daemon.requestLoop()
