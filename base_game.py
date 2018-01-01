from itertools import combinations_with_replacement
from random import shuffle


class Player:
    def __init__(self):
        self.hand = []

    def take_turn(self, game_state):


    def play(self, piece):
        pass

def deal_game(player_list):
    global game_state
    all_pieces = list(combinations_with_replacement(range(10), 2))
    shuffle(all_pieces)
    pieces_per_player = len(all_pieces)//len(player_list)
    for player in player_list:
        player.hand = all_pieces[:pieces_per_player]
        all_pieces = all_pieces[pieces_per_player:]
    game_state = [all_pieces[0]]

def create_players(number_of_players):
    l = []
    for i in range(number_of_players):
        l.append(Player())
    return l




if __name__ == "__main__":
    list_players = create_players(4)
    deal_game(list_players)
    while 0 < min(len(player.hand) for player in list_players):
        for player in list_players:
            player.take_turn(game_state)
            print(game_state)
