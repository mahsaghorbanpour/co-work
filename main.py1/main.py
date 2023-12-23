import random
def total_11(num1, num2):
    result = num1 + num2
    if result == 11:
        return True
    else:
        return False
def generate_game_set(suits,cards):
    deck = set()
    for suit in suits:
        for card in cards:
            deck.add((card, "of", suit))
    return deck
suits = ["del", "khesht", "geshniz", "pick"]
faces = ["shah", "bi bi", "tak", "sarbaz"]
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
card = faces + nums
gameset = generate_game_set(suits, card)
earth = []
amin = []
mahsa = []
win_amin = []
win_mahsa = []
for i in range(4):
    card = random.choice(list(gameset))
    earth.append(card)
    gameset.remove(card)
while len(gameset) != 0:
    for i in range(4):
        card = random.choice(list(gameset))
        amin.append(card)
        gameset.remove(card)
    for _ in range(4):
        card = random.choice(list(gameset))
        mahsa.append(card)
        gameset.remove(card)
    for k in range(4):
        print(earth)
        print(amin)
        user_input =int(input("please select the card index :"))
        card = amin[user_input]
        amin.remove(card)
        for j in earth:
            if total_11(j, card) == True:
                win_amin.append(j)
                win_amin.append(card)
            else:
                earth.append(card)
        print(earth)
        print(mahsa)
        user_input =int(input("please select the card index :"))
        card = mahsa[user_input]
        mahsa.remove(card)
        for a in earth:
            if total_11(a, card) == True:
                win_mahsa.append(a)
                win_mahsa.append(card)
            else:
                earth.append(card)


