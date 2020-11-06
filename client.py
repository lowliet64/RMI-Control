import Pyro4
import time
import os

ns = Pyro4.locateNS()
uri = ns.lookup('obj')

o = Pyro4.Proxy(uri)
o.getPosicao()

while True:
    print("#-------------mini Aeroporto-------------#")
    print("# ***localização atual -> [", o.getLocalizacao(), "]")
    print("#------------------------------------------------------#")
    print("# Digite uma opção de lugar para viajar")
    print("# 1 - Rio Grande do Norte")
    print("# 2 - Bahia ")
    print("# 3 - São Paulo")
    print("# 4 - Acre")
    opt = int(input())
    o.irAteDestino(opt)

    os.system('cls')
    print("carregando.....")
    time.sleep(3)

print('✈')
