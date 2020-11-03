import Pyro4

@Pyro4.expose
class Aviao:
    def saludar(self):
        return 'aviao sei la'


daemon = Pyro4.Daemon()
uri = daemon.register(Aviao)
ns = Pyro4.locateNS()
ns.register('obj', uri)

print(uri)
daemon.requestLoop()
