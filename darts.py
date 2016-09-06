import json
import datetime


class Player:
    def __init__(self, name):
        self.name = name


class Game:
    attempts_count = 10

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_attempts = {}
        self.player2_attempts = {}

    def set_attempt(self, player, ind, scores):
        # you have 10 attempts per game
        key = "attempt_" + str(ind)

        if player == self.player1:
            self.player1_attempts[key] = scores
        elif player2 == self.player2:
            self.player2_attempts[key] = scores
        else:
            print('invalid player')

    def to_dict(self):
        return {
            'date': str(datetime.datetime.now()),
            self.player1.name: self.player1_attempts,
            self.player2.name: self.player2_attempts
        }

    def to_json(self, player):
            return json.dumps(self.to_dict(), sort_keys=True, indent=4)

    def save(self):
        games_file = open("games_file.json", 'r')
        file_data = games_file.read()
        games_file.close()

        games_file = open("games_file.json", 'w')
        all_games_dict = {}
        if len(file_data) == 0:
            all_games_dict = {
                "games": []
            }
        else:
            all_games_dict = json.loads(file_data)
        all_games_dict['games'].append(self.to_dict())
        all_games_json = json.dumps(all_games_dict, sort_keys=True, indent=4) 
        games_file.write(all_games_json)
        games_file.close()

player1 = Player('player1')
player2 = Player('player2')
game = Game(player1, player2)

for i in range(1,11):
    game.set_attempt(player1, i, i*10)
for i in range(1,11):
    game.set_attempt(player2, i, i*20)
game.save()
import tkinter
width = "500"
height = "500"

# Code to add widgets will go here...
def submit(player1_entry, player2_entry):
    print(player1_entry)
    print(player2_entry)

top = tkinter.Tk()
top.geometry('{}x{}'.format(width, height))

submit_result = tkinter.Button(top, width=20, text ="Try 1", command = lambda: submit(player1_entry.get(), player2_entry.get()))


darts_label = tkinter.Label(top, text="DARTS", width=30)


player1_label = tkinter.Label(top, text=player1.name)
player1_entry = tkinter.Entry(top, bd =5)

player2_label = tkinter.Label(top, text=player2.name)
player2_entry = tkinter.Entry(top, bd =5)

submit_result.grid(row=3, column=1)

player1_label.grid(row=1, column=0)
player1_entry.grid(row=2, column=0)

player2_label.grid(row=1, column=2)
player2_entry.grid(row=2, column=2)

darts_label.grid(row=0, column=1)

top.mainloop()