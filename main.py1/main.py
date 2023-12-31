import random


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
faces = ["shah", "bi bi", "tak", "sarbaz"]
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
card = faces + nums

gameset = generate_game_set(suits, card)
print(gameset)

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
        is_win = False
        for j in earth:
            print("card of amin : ", card)
            print("card of j : ", j)
            if total_11(j[0], card[0]) == True:
                win_amin.append(j)
                win_amin.append(card)
                is_win = True
                break
        if is_win == False:
            earth.append(card)

        print("==================================")
        print("cards of earth = ", earth)
        print("cards of mahsa = ", mahsa)
        user_input =int(input("please select the card index :"))
        card = mahsa[user_input]
        mahsa.remove(card)
        mahsa_flag = False
        for a in earth:
            if total_11(a[0], card[0]) == True:
                win_mahsa.append(a)
                win_mahsa.append(card)
                mahsa_flag = True
                break
        if mahsa_flag == False:
            earth.append(card)
        print("one set finished")
        print("wins of amin", win_amin)
        print("wins of mahsa", win_mahsa)

#
# def mahsa(user_color, user_age):
#     message = "{} is very beauty".format(user_color)
#     print(message)
#     new_age = user_age + 1
#     return new_age
#
#
# def amin(job, experience):
#     new_ex = experience + 1
#     message = "amin is a {}".format(job)
#     print(message)
#     return new_ex
#
# message ="This is our scope sample"
#
# print("welcome {}".format(message))
#
# amin_job = "programmer"
# amin_exp = 2
#
# mahsa_color = "dark red"
# mahsa_age = 20
#
# amin_result = amin(job=amin_job, experience= amin_exp)
# mahsa_result=mahsa(user_color=mahsa_color, user_age= mahsa_age)
#
#
# print(message)
# print(amin_result)
# print(mahsa_result)
#
#
#
#
#
#
#







