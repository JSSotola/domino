from itertools import combinations_with_replacement
from random import shuffle
from players import random_turn, min_turn, max_turn


class Game:
    def __init__(self):
        self.table = []

    def deal(self, player_list):
        all_pieces = list(combinations_with_replacement(range(10), 2))
        shuffle(all_pieces)
        pieces_per_player = len(all_pieces) // len(player_list)
        for player in player_list:
            player.hand = all_pieces[:pieces_per_player]
            all_pieces = all_pieces[pieces_per_player:]
        self.table = [all_pieces[0]]

    def start_game(self):
        print("START TABLE:")
        print(self.table)
        while min(len(player.hand) for player in list_players) > 0 and not all(player.passed for player in list_players):
            for player in list_players:
                player.take_turn(self.table)

                print("TABLE:")
                print(self.table)

        print("---------")
        leaderboard = sorted(list_players, key=lambda player: player.score())
        print(leaderboard)
        print(list(player.score() for player in leaderboard))
        # for player in list_players:


    def play(self, player, piece):

        player.passed = False
        if piece == "PASS":
            player.passed = True
        elif self.table[0][0] in piece:
            end = self.table[0][0]
            player.hand.remove(piece)
            if end != piece[1]:
                piece = (piece[1], piece[0])
            self.table = [piece] + self.table
        elif self.table[-1][1] in piece:
            end = self.table[-1][1]
            player.hand.remove(piece)
            if end != piece[0]:
                piece = (piece[1], piece[0])
            self.table.append(piece)
        else:
            raise Exception("WRONG TURN", piece, "is not a valid move!\nThe game state is:", self.table)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.passed = False

    def take_turn(self, game_state):
        #  PLAYER CODE HERE
        piece = random_turn(self, game_state)
        #
        game.play(self, piece)

    def score(self):
        return sum(sum(piece) for piece in self.hand)

def create_players(number_of_players):
    player_list = []
    player_names = ["franta", "pepa", "honza", "alfred"]
    #  TODO REPLACE THIS WITH IMPORT PLAYERS
    for i in range(number_of_players):
        player_list.append(Player(player_names[i]))
    return player_list


if __name__ == "__main__":
    list_players = create_players(4)
    game = Game()
    game.deal(list_players)
    game.start_game()
