import random


# class Player:
# 	def __init__(self, hand, _turn):
# 		self.hand = hand
# 		self._turn = _turn

# 	def turn(self, table):
# 		return self._turn(self, table)

def possible_turns(hand, first, last):
    possible = []
    for piece in hand:
        if piece[0] == first or piece[1] == last:
            possible.append(piece)

    return possible


# hraje náhodně
def random_turn(self, table):
    firstNum = table[0][0]
    lastNum = table[-1][1]
    possible = possible_turns(self.hand, firstNum, lastNum)
    if len(possible) == 0:
        return "PASS"
    else:
        return random.choice(possible)


# hraje vždy s největším součtem puntíků
def max_turn(self, table):
    firstNum = table[0][0]
    lastNum = table[-1][1]
    possible = possible_turns(self.hand, firstNum, lastNum)
    possible = sorted(possible, key=lambda x: x[0] + x[1], reverse=True)
    return possible[0]


# snaží se pokládat co nejmenší koncový kámen
def min_turn(self, table):
    firstNum = max(table[0][0], table[-1][1])
    lastNum = min(table[0][0], table[-1][1])
    possible = possible_turns(self.hand, firstNum, lastNum)

    # possible = sorted(possible, key=lambda x: 1 if x[0]==firstNum or x[1]==firstNum else 0, reverse=True)
    return possible[0]

# player = Player([(1,2), (1,3), (4,5)], max_turn)
# print(player.turn([(1,5), (5,5)]))
