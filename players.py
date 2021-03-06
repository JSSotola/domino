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
        if first in piece or last in piece:
            possible.append(piece)

    return possible


# hraje náhodně
def random_turn(self, table):
    first_num = table[0][0]
    last_num = table[-1][1]
    possible = possible_turns(self.hand, first_num, last_num)
    # print(self.name+" hand: ", self.hand)
    # print(self.name+" possible: ", possible)
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
    if len(possible) == 0:
        return "PASS"
    else:
        return possible[0]

# snaží se pokládat co nejmenší koncový kámen
def min_turn(self, table):
    firstNum = max(table[0][0], table[-1][1])
    lastNum = min(table[0][0], table[-1][1])
    possible = possible_turns(self.hand, firstNum, lastNum)

    possible = sorted(possible, key=lambda p: 10+min(p) if firstNum in p else min(p), reverse=True)
    if len(possible) == 0:
        return "PASS"
    else:
        return possible[0]
