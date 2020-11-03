import Pyro4

ns = Pyro4.locateNS()
uri = ns.lookup('obj')

o = Pyro4.Proxy(uri)
print(o.saludar())
