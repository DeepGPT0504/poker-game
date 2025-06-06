import random

ranks = "23456789TJQKA"
suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)