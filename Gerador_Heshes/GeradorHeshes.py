import hashlib

string = input("Digite um texto: ")

resultado = hashlib.md5(string.encode('utf-8'))

print("O hash da string é: ", resultado.hexdigest())