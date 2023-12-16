import random
def generate_game_set(suits,cards):
    deck = set()
    for suit in suits:
        for card in cards:
            deck.add((card , "of" , suit ))
    return deck
suits = ["del" , "khesht" , "geshniz" , "pick"]
faces = ["shah" , "bi bi" , "tak" , "sarbaz"]
nums = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
card = faces + nums
gameset = generate_game_set (suits,card)
amin = []
mahsa = []
for i in range(5):
    card = random.choice(list(gameset))
    amin.append(card)
    gameset.remove(card)
for _ in range(5):
    card = random.choice(list(gameset))
    mahsa.append(card)
    gameset.remove(card)


