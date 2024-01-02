import random


# What is purpose of this function ?
# What is list_of_point?
def calculate_point(list_of_point):
    player_point = 0
    for point in list_of_point:
        if point[2] == "clubs":
            player_point += 1
    return player_point


# what is purpose of this function?
def check_win(card1, card2):
    if (type(card1) is int) and (type(card2) is int):
        result = card1 + card2

        if result == 11:
            return True
        else:
            return False
    elif (type(card1) is str) and (type(card2) is str):
        if card2 == card1:
            return True
        else:
            return False
    else:
        return False


# why we generate set for our cards? why we don't use list instead of that?
# suits :
# cards :
def generate_game_set(suits, cards):
    deck = set()
    for suit in suits:
        for card in cards:
            deck.add((card, "of", suit))
    return deck


suits_of_cards = ["hearts", "diamonds", "clubs", "spades"]
faces_cards = ["King", "Queen", "Jack"]
numbers_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_of_cards = faces_cards + numbers_cards

# which variable of generate_game_set fill in game_cards_set ?
# can we use deck here? why?
game_cards_set = generate_game_set(suits_of_cards, list_of_cards)

cards_of_earth = []
cards_of_amin = []
cards_of_mahsa = []
points_of_amin = []
points_of_mahsa = []

# what is purpose of this for ?
for _ in range(4):
    # why we convert game_cards_set to list?
    earth_random_card = random.choice(list(game_cards_set))
    cards_of_earth.append(earth_random_card)
    game_cards_set.remove(earth_random_card)

while len(game_cards_set) != 0:
    # what is purpose of this for ?
    for _ in range(4):
        amin_random_card = random.choice(list(game_cards_set))
        cards_of_amin.append(amin_random_card)
        game_cards_set.remove(amin_random_card)
    # what is purpose of this for ?
    for _ in range(4):
        mahsa_random_card = random.choice(list(game_cards_set))
        cards_of_mahsa.append(mahsa_random_card)
        game_cards_set.remove(mahsa_random_card)
    # what is purpose of this for ?
    for _ in range(4):
        print("====================================================")

        print("cards of earth = ", cards_of_earth)
        print("cards of amin =", cards_of_amin)
        amin_selected_index = int(input("please select the card index :"))
        amin_selected_card = cards_of_amin[amin_selected_index]
        cards_of_amin.remove(amin_selected_card)
        jack_winner_list = []
        # what is purpose of this if?
        if amin_selected_card[0] == "Jack":
            # what is purpose of this flag?
            is_jack_win_card = False
            for index in range(len(cards_of_earth)):
                earth_card = cards_of_earth[index]
                # why we select 0th index of earth card ?
                if (type(earth_card[0]) is int) or (earth_card[0] == "Jack"):
                    points_of_amin.append(earth_card)
                    jack_winner_list.append(earth_card)
                    is_jack_win_card = True
                else:
                    continue
            # why i didn't write   if is_jack_win_card == True:
            if is_jack_win_card:
                points_of_amin.append(amin_selected_card)
                # what is win_card ?
                for win_card in jack_winner_list:
                    cards_of_earth.remove(win_card)
                jack_winner_list = []
            else:
                cards_of_earth.append(amin_selected_card)
        else:
            # what is purpose of this flag?
            is_card_win = False
            for card in cards_of_earth:
                # why i didn't write total_11(card[0], amin_selected_card[0])== True
                # what is total_11 return?
                if check_win(card[0], amin_selected_card[0]):
                    points_of_amin.append(card)
                    cards_of_earth.remove(card)
                    points_of_amin.append(amin_selected_card)
                    is_card_win = True
                    break
            # we could write  is_card_win == False  :  not is_card_win
            if not is_card_win:
                cards_of_earth.append(amin_selected_card)

        print("====================================================")
        print("cards of earth = ", cards_of_earth)
        print("cards of mahsa = ", cards_of_mahsa)
        mahsa_selected_index = int(input("please select the card index :"))
        mahsa_selected_card = cards_of_mahsa[mahsa_selected_index]
        cards_of_mahsa.remove(mahsa_selected_card)
        # is it ok we used is_jack_win_card in both amin and mahsa turns?
        is_jack_win_card = False
        if mahsa_selected_card[0] == "Jack":
            jack_winner_list = []
            for card_index in range(len(cards_of_earth)):
                # is it ok we used earth_card in both amin and mahsa turns?
                earth_card = cards_of_earth[card_index]
                if type(earth_card[0]) is int or earth_card[0] == "sarbaz":
                    points_of_mahsa.append(earth_card)
                    jack_winner_list.append(earth_card)
                    is_jack_win_card = True
            if is_jack_win_card:
                points_of_mahsa.append(mahsa_selected_card)
                for win_card in jack_winner_list:
                    cards_of_earth.remove(win_card)
                jack_winner_list = []

            else:
                cards_of_earth.append(mahsa_selected_card)
        else:
            is_card_win = False
            for earth_card in cards_of_earth:
                if check_win(earth_card[0], mahsa_selected_card[0]):
                    points_of_mahsa.append(earth_card)
                    points_of_mahsa.append(mahsa_selected_card)
                    cards_of_earth.remove(earth_card)
                    is_card_win = True
                    break
            if is_card_win == False:
                cards_of_earth.append(mahsa_selected_card)
        print("one set finished")
        print("wins of amin", points_of_amin)
        print("wins of mahsa", points_of_mahsa)

point_of_amin = calculate_point(points_of_amin)
point_of_mahsa = calculate_point(points_of_mahsa)

if point_of_amin > point_of_mahsa:
    print("Amin is win game with grade :", point_of_amin)
else:
    print("Mahsa is win game with grade :", point_of_mahsa)


# what is scope of variable player_point?
# what is scope of variable card2?
# can we use card2 in check_win function?
