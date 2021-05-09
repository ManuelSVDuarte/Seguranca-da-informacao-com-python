import socket 
import sys

def main():
    try: 
        conec = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("Falha na conexão")
        print("Erro: {}".format(erro))
        sys.exit()
    
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o hostel ou IP a ser conectado: ")
    PortaAlvo = input("Digita a porta: ")
    
    try:
        conec.connect((HostAlvo, int(PortaAlvo)))
        print("Conexão TCP realizada com sucesso, Hoste Alvo")


