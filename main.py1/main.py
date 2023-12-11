def generate_game_set(suits,card):
    deck = set()
    for suit in suits:
        for card in faces + nums:
            deck.add((card , "of" , suit ))
    return deck
suits = ["del" , "khesht" , "geshniz" , "pick"]
faces = ["shah" , "bi bi" , "tak" , "sarbaz"]
nums = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
card = faces + nums
gameset = generate_game_set (suits,card)
print(gameset)

