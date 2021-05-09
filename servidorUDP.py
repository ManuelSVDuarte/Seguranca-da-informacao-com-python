import socket

conecServe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso ")
host = 'localhost'
port = 5432

conecServe.bind((host, port))
mensagem = 'Servidor: conexão realizada com sucesso'

while 1:
    dados, ender = conecServe.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem: ')
        conecServe.sendto(dados + (mensagem.ecode()), ender)

