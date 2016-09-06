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
        elif player == self.player2:
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
