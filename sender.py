from ipaddress import ip_address
import socket
import struct

MCAST_GRP = '224.0.0.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

host = socket.gethostbyname(socket.gethostname())

sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))

sock.sendto(b'Hello World!', (MCAST_GRP, MCAST_PORT))
