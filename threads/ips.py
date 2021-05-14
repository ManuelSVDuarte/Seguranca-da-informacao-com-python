import ipaddress 

ip = "192.168.0.21/24"

rede = ipaddress.ip_network(ip, strict=False)

print(rede)