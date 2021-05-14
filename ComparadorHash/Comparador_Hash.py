import hashlib
from typing import Hashable

def compararhashs(arquivo1, aquivo2):
    hash1 = hashlib.new('ripemd160')
    hash2 = hashlib.new('ripemd160')
    
    hash1.update(open(arquivo1, 'rb').read())
    hash2.update(open(arquivo2, 'rb').read())
 
    if hash1.digest() != hash2.digest():
       return print(f'O arquivo {arquivo1} é diferente do arquivo {arquivo2} \n Hash do arquivo 1: {hash1.hexdigest()} \n Hash do arquivo 2: {hash2.hexdigest()}')
    else:
      return print(f'O arquivo {arquivo1} é igual ao arquivo {arquivo2} \n Hash do arquivo 1: {hash1.hexdigest()} \n Hash do arquivo 2: {hash2.hexdigest()}')



arquivo1 = input("Digite o nome do primeiro arqivo: ")
arquivo2 = input("Digite o nome do segundo arqivo: ")

compararhashs(arquivo1, arquivo2)
