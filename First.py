import random

ranks = "23456789TJQKA"
suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)

num_players = 4
print(f"플레이어 수: {num_players}명")

players = { }
for i in range(1, num_players +1):
    print()
