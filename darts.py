import json
import tkinter
import datetime


class Player:
    def __init__(self, name):
        self.name = name


class Game:
    attempts_count = 10

    width = "500"
    height = "500"

    def __init__(self):
        self.current_attempt = 1
        self.game_id = 0

        games_file = open("games_file.json", 'r')
        file_data = games_file.read()
        games_file.close()

        if len(file_data):
            json_data = json.loads(file_data)
            self.game_id = len(json_data['games'])

        self.setup_start_page()

    def quit(self):
        self.save()
        self.window.quit()

    def press_submit_button(self, player1_entry, player2_entry):
        print(self.current_attempt)
        print(player1_entry)
        print(player2_entry)
        if self.current_attempt > 10:
            self.quit()
        self.set_attempt(self.player1, self.current_attempt, player1_entry)
        self.set_attempt(self.player2, self.current_attempt, player2_entry)
        self.next_attempt()

    def set_players_names(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player1_attempts = {}
        self.player2_attempts = {}
        for widget in self.window.winfo_children():
            widget.destroy()
        self.setup_gui()

    def setup_start_page(self):
        self.window = tkinter.Tk()

        player1_label = tkinter.Label(self.window, text="Player 2")
        player1_entry = tkinter.Entry(self.window, bd=5)

        player2_label = tkinter.Label(self.window, text="Player 1")
        player2_entry = tkinter.Entry(self.window, bd=5)

        self.set_names_button = tkinter.Button(
            self.window,
            width=20,
            text="Try " + str(self.current_attempt),
            command=lambda: self.set_players_names(player1_entry.get(), player2_entry.get()))

        player1_label.grid(row=1, column=0)
        player1_entry.grid(row=2, column=0)

        player2_label.grid(row=1, column=2)
        player2_entry.grid(row=2, column=2)

        self.set_names_button.grid(row=3, column=1)
        self.window.mainloop()

    def setup_gui(self):
        # Game GUI
        self.window.geometry('{}x{}'.format(self.width, self.height))

        self.submit_result = tkinter.Button(self.window,
                                            width=20,
                                            text="Try " + str(self.current_attempt),
                                            command=lambda: self.press_submit_button(self.player1_entry.get(),
                                                                                     self.player2_entry.get()))

        self.darts_label = tkinter.Label(self.window,
                                         text="DARTS",
                                         width=30)

        self.player1_label = tkinter.Label(self.window, text=self.player1.name)
        self.player1_entry = tkinter.Entry(self.window, bd=5)

        self.player2_label = tkinter.Label(self.window, text=self.player2.name)
        self.player2_entry = tkinter.Entry(self.window, bd=5)

        self.submit_result.grid(row=3, column=1)

        self.player1_label.grid(row=1, column=0)
        self.player1_entry.grid(row=2, column=0)

        self.player2_label.grid(row=1, column=2)
        self.player2_entry.grid(row=2, column=2)

        self.darts_label.grid(row=0, column=1)

    def next_attempt(self):
        self.current_attempt += 1

    def set_attempt(self, player, ind, scores):
        # you have 10 attempts per game
        key = "attempt_" + str(ind)

        if player == self.player1:
            self.player1_attempts[key] = scores
        elif player == self.player2:
            self.player2_attempts[key] = scores
        else:
            print('invalid player')

    def to_dict(self):
        return {
            'date': str(datetime.datetime.now()),
            'game_id': str(self.game_id),
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
