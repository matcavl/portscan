import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.6)

ip = input("Digite o ip ou endereço: ")
rangeInicial = int(input("Digite a porta inicial: "))
rangeFinal = int(input("Digite a porta final: "))

for port in range(rangeInicial, rangeFinal+1):
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.settimeout(0.6)
	result = connection.connect_ex((ip, port))
	if result == 0:
		print (port, "open")
	else:
		print(port, "closed")
