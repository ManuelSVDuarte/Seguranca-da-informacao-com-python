from threading import Thread, ThreadError
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print('piloto: {}  km: {} \n'.format(piloto, trajeto))



t_carro1 = Thread(target=carro, args=[1, 'Piloto 1'])
t_carro2 = Thread(target=carro, args=[1.5, 'Piloto 2'])

t_carro1.start()
t_carro2.start()

