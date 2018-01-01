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

    def start_game(self):
        while 0 < min(len(player.hand) for player in list_players): #todo: all passed:
            for player in list_players:
                player.take_turn(self.table)

                print(self.table)

    def play(self, player, piece):
        player.passed = False
        if piece == "PASS":
            player.passed = True
        elif self.table[0][0] in piece:
            end = self.table[0][0]
            if end != piece[1]:
                piece = (piece[1], piece[0])
            self.table = [piece] + self.table
        elif self.table[-1][1] in piece:
            end = self.table[-1][1]
            if end != piece[0]:
                piece = (piece[1], piece[0])
            self.table.append(piece)
        else:
            raise Exception("WRONG TURN", piece, "is not a valid move!\nThe game state is:", self.table)
        player.hand.remove(piece)


class Player:
    def __init__(self):
        self.hand = []
        self.passed = False

    def take_turn(self, game_state):
        #  PLAYER CODE HERE
        #
        #
        game.play(self, self.hand[0])



def create_players(number_of_players):
    l = []
    #  TODO REPLACE THIS WITH IMPORT PLAYERS
    for i in range(number_of_players):
        l.append(Player())
    return l


if __name__ == "__main__":
    list_players = create_players(4)
    game = Game()
    game.deal(list_players)
    game.start_game()
