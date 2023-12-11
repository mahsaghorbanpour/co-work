def generate game set(suits,faces+nums):
    card = random.choice(list(deck))
    deck.remove(card)
    suits = ["del" , "khesht" , "geshniz" , "pick"]
    faces = ["shah" , "bi bi" , "tak" , "sarbaz"]
    nums = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
deck = set()
for suit in suits:
    for card in faces + nums:
        deck.add((card , "of" , suit ))
return deck
gameset = generate game set (suits,face+nums)
print gameset

