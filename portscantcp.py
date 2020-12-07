import socket
import sys

try:
	ip = sys.argv[1]
	rangeInitial = sys.argv[2]
	finalRange = sys.argv[3]
	time = int(sys.argv[4])

except:
	print("Missing Values")
	print("Usage: portscan.py <initialPort> <endPort> <time (min value: 1 - max value: 6>")
	print("Example: portscan.py google.com 1 65535 5")
	sys.exit(1)

for port in range(int(rangeInitial), int(finalRange)+1):
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.settimeout(time*0.10)
	result = connection.connect_ex((ip, port))

	if result == 0:
		print("IP: " + ip + " Port: " + str(port), "Open")
	else:
		print("IP: " + ip + " Port: " + str(port), "Closed")

