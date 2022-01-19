import socket
import threading
import CONSTANTS

# Connection Data



class Server:
    Servers = []
    host = CONSTANTS.HOME_SERVER_LOCAL_HOST_IPV4
    port = CONSTANTS.PORT

    # Starting Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    # Lists For Clients and Their Nicknames
    # FUTURE INFORMATION ON EACH CLIENT SHOULD SHOW: HASH VALUE, SIZE, FILENAME, IP,
    clients = []
    nicknames = []

    '''BET INFO'''
    bets = [{}]
    # Sending Messages To All Connected Clients
    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    # Handling Messages From Clients
    def handle(self, client):
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)  # Biggest msg size?
                self.broadcast(message)
            except:
                # Removing And Closing Clients
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast('{} left!'.format(nickname).encode('utf-8'))
                self.nicknames.remove(nickname)
                break

    def receive(self):
        while True:
            # Accept Connection
            print("Waiting for connections...")
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))
            print(f"Hosting from {CONSTANTS.HOME_SERVER_LOCAL_HOST_IPV4}")
            # Request And Store Nickname
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            self.broadcast("{} joined! ".format(nickname).encode('utf-8'))
            client.send('Connected to server!'.encode('utf-8'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()


Server = Server()
Server.receive()