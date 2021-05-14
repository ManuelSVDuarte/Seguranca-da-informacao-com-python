import socket

conecUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso ")

host = 'localhost'
porta = 5433
mensagem = 'Teste conexão '

try:
    print('Cliente: ' + mensagem)
    conecUDP.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = conecUDP.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados )

finally:
    print("Cliente: Fanalizando a conexão")
    conecUDP.close()