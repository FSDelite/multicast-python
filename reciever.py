import socket


MCAST_GRP = '224.0.0.1'
MCAST_PORT = 5007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
try:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except AttributeError:
    pass
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

print(socket.SOL_IP)

sock.bind(('', MCAST_PORT))
host = socket.gethostbyname(socket.gethostname())
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF,
                socket.inet_aton(host))
#Entrar no grupo
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                socket.inet_aton(MCAST_GRP) + socket.inet_aton(host))

while 1:
    try:
        data, addr = sock.recvfrom(1024)
    except (socket.error):
        print('Exception')
    else:
        print(data)