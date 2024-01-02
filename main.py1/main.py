import random


def calculate_point(list_of_point):
    point = 0
    for p in list_of_point:
        if p[2] == "geshniz":
            point+=1
    return point


def total_11(num1, num2):
    if (type(num1) is int) and (type(num2) is int):
        result = num1 + num2

        if result == 11:
            return True
        else:
            return False
    elif (type(num1) is str) and (type(num2) is str):
        if num2 == num1:
            return True
        else:
            return False
    else:
        return False


def generate_game_set(suits,cards):
    deck = set()
    for suit in suits:
        for card in cards:
            deck.add((card, "of", suit))
    return deck



suits = ["del", "khesht", "geshniz", "pick"]
faces = ["shah", "bi bi", "sarbaz"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
        print("==================================")

        print("cards of earth = ", earth)
        print("cards of amin =", amin)
        user_input =int(input("please select the card index :"))
        card = amin[user_input]
        amin.remove(card)
        sarbaz_winner= []
        if card[0] == "sarbaz":
            number_existance = False
            for m in range(len(earth)):
                earth_card = earth[m]
                if (type(earth_card[0]) is int) or (earth_card[0] == "sarbaz"):
                    win_amin.append(earth_card)
                    sarbaz_winner.append(earth_card)
                    number_existance = True
                else:
                    continue
            if number_existance == True:
                win_amin.append(card)
                for s in sarbaz_winner:
                    earth.remove(s)
                sarbaz_winner = []
            else:
                earth.append(card)
        else:
            is_win = False
            for j in earth:
                if total_11(j[0], card[0]) == True:
                    win_amin.append(j)
                    earth.remove(j)
                    win_amin.append(card)
                    is_win = True
                    break
            if is_win == False:
                earth.append(card)

        print("==================================")
        print("cards of earth = ", earth)
        print("cards of mahsa = ", mahsa)
        user_input = int(input("please select the card index :"))
        card = mahsa[user_input]
        mahsa.remove(card)
        msarbaz = False
        if card[0] == "sarbaz":
            msarbaz_winner = []
            for l in range(len(earth)):
                m_earth_card = earth[l]
                if type(m_earth_card[0]) is int or m_earth_card[0] == "sarbaz":
                    win_mahsa.append(m_earth_card)
                    msarbaz_winner.append(m_earth_card)
                    msarbaz = True
            if msarbaz == True:
                win_mahsa.append(card)
                for s in msarbaz_winner:
                    earth.remove(s)
                msarbaz_winner = []

            else:
                earth.append(card)
        else:
            mahsa_flag = False
            for a in earth:
                if total_11(a[0], card[0]) == True:
                    win_mahsa.append(a)
                    win_mahsa.append(card)
                    earth.remove(a)
                    mahsa_flag = True
                    break
            if mahsa_flag == False:
                earth.append(card)
        print("one set finished")
        print("wins of amin", win_amin)
        print("wins of mahsa", win_mahsa)

point_of_amin = calculate_point(win_amin)
point_of_mahsa = calculate_point(win_mahsa)

if point_of_amin > point_of_mahsa:
    print("Amin is win game with grade :", point_of_amin)
else:
    print("Mahsa is win game with grade :", point_of_mahsa)
