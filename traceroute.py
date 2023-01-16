import socket
import random
import struct


def trace(dest: str):
    try:
        dest_ip = socket.gethostbyname(dest)
    except socket.error:
        raise IOError('Unable to resolve {}.'.format(dest))
    port = random.choice(range(33434, 33535))

    print('traceroute to {} ({}) using port {}'.format(
        dest,
        dest_ip,
        port
    ))

    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1

    while True:
        receiver = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        receiver.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, struct.pack("ll", 5, 0))

        sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        try:
            receiver.bind(('', port))
        except socket.error as e:
            raise IOError('Unable to bind receiver socket to port {}: {}'.format(port, e))

        sender.sendto(b'', (dest, port))

        print('{:<4}'.format(ttl), end='')

        ip = None
        is_found = False
        tries = 0

        while not is_found and tries < 3:
            try:
                if tries != 0:
                    print('    ', end='')
                tries += 1

                _, ip = receiver.recvfrom(1024)
                ip = ip[0]
                is_found = True

                try:
                    name = socket.gethostbyaddr(ip)[0]
                except socket.error:
                    name = ip

                print('{:<15} ({})'.format(ip, name))
            except socket.error:
                print('*'.format(ttl))

        sender.close()
        receiver.close()

        ttl += 1
        if ip == dest_ip or ttl > 64:
            break


if __name__ == '__main__':
    dst = input('Enter the address to traceroute: ')
    trace(dst)
