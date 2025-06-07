import random


# 1. 카드 설정
ranks = "23456789TJQKA"
suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)

# 2. 플레이어 설정
num_players = 4
players = {}
for i in range(1, num_players + 1):
    give_deck = [deck.pop() for _ in range(2)]
    players[f'Player {i}'] = give_deck

# 3. 커뮤니티 카드 설정
community_cards = [deck.pop() for _ in range(5)]


