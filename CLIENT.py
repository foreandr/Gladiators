import socket
import threading
import CONSTANTS
import json

class Client:
    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((CONSTANTS.HOME_SERVER_LOCAL_HOST_IPV4 , CONSTANTS.PORT))

    def __init__(self):
        self.nickname = input("Choose your nickname: ")
        self.bets = []
        self.bet_num_people = int(input("1 or 2"))
        self.get_betters()

        print(self.bet_name1)
        print(self.bet_name2)

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

    def generate_bet_details(self):
        self.bet_meta_details = {
            "Better": self.nickname,
            "First": self.bet_name1,
            "Second": self.bet_name2,
            "Details": self.create_bet()
        }
        self.bet_meta_details = json.dumps(self.bet_meta_details)
        print(self.bet_meta_details)
        print(type(self.bet_meta_details))


    def create_bet(self):
        self.bet_details = {}
        round_choices = [1, 2, 3, 4, 5]
        finish_choices = ['KO', 'SUB', 'DECISION']
        bet_ratio_choies_temp = [1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.7, 1.8, 1.9, 2.0]

        '''CREATE THE PARTICULARS OF THE BET'''
        round_choice = round_choices[0] #NTH ROUND
        finish_choice = finish_choices[0] #NTH FINISH
        bet_choice = bet_ratio_choies_temp[0]

        self.bet_details = {
            "ROUND": round_choice ,
            "FINISH": finish_choice,
            "Ratio": bet_choice
        }
        return self.bet_details
    def get_betters(self):
        #print(self.bet_num_people)
        #print(type(self.bet_num_people))

        if self.bet_num_people == 1:
            self.bet_name1 = input("Name of person1")
            self.bet_name2 = ""
        elif self.bet_num_people == 2:
            self.bet_name1 = input("Name of person1")
            self.bet_name2 = input("Name of person2")

        self.generate_bet_details()
    def breadcast_bet(self):
        while True:
            self.client.send(self.bet_meta_details.encode('ascii'))

    def print_details(self):
        print(self.bet_meta_details)


Client = Client()
Client.print_details()
Client.breadcast_bet()
Client.run()
