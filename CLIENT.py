import socket
import threading
import CONSTANTS

class Client:
    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((CONSTANTS.HOME_SERVER_LOCAL_HOST_IPV4 , CONSTANTS.PORT))

    def __init__(self):
        self.nickname = input("Choose your nickname: ")
        self.bets = []
        self.bet_num_people = int(input("1 or 2"))
        self.func()
        '''
        
           
        elif self.bet_num_people == 2:
            self.bet_name1 = input("Name of person1")
            self.bet_name2 = input("Name of person2")
        
        '''

    # Listening to Server and Sending Nickname
    def receive(self):
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("An error occured!")
                self.client.close()
                break
    # Sending Messages To Server
    def write(self):
        while True:
            message = '{}: {}'.format(self.nickname, input(''))
            self.client.send(message.encode('ascii'))
    def run(self):
        # Starting Threads For Listening And Writing
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

        self.write_thread = threading.Thread(target=self.write)
        self.write_thread.start()

    '''LAMBDA TESTS'''
    def func(self):
        #print(self.bet_num_people)
        #print(type(self.bet_num_people))

        if self.bet_num_people == 1:
            print("hello world")
        elif self.bet_num_people == 2:
            print("big tiddie")
            #self.bet_name1 = input("Name of person1")
            #self.bet_name2 = input("Name of person2")






Client = Client()
Client.run()