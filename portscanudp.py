import socket

ip = input("IP: ")

while True:
    port = input('Port: ')
    if(port == 'exit'): break
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        print('Port {} open'.format(port))
    except:
        print('Port {} not open'.format(port))
    s.close()
