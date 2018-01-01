from itertools import combinations_with_replacement
from random import shuffle

class Game:
    def __init__(self):
        self.table = []

    def deal(self, player_list):
        all_pieces = list(combinations_with_replacement(range(10), 2))
        shuffle(all_pieces)
        pieces_per_player = len(all_pieces)//len(player_list)
        for player in player_list:
            player.hand = all_pieces[:pieces_per_player]
            all_pieces = all_pieces[pieces_per_player:]
        self.table = [all_pieces[0]]

    def play(self):
        while 0 < min(len(player.hand) for player in list_players): #todo: all passed:
            for player in list_players:
                player.take_turn(self.table)

                print(self.table)

class Player:
    def __init__(self):
        self.hand = []

    def take_turn(self, game_state):
        self.play(self.hand[0])
        return True

    def play(self, piece):
        if game_state[0][0] in piece:
            end = game_state[0][0]
        elif game_state[-1][1] in piece:
            end = game_state[-1][1]

        self.hand.remove(piece)

def create_players(number_of_players):
    l = []
    for i in range(number_of_players):
        l.append(Player())
    return l

if __name__ == "__main__":
    list_players = create_players(4)
    game = Game()
    game.deal(list_players)
    game.play()
