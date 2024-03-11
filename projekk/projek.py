import random

import time

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='demogame',
         user='root',
         password='ro0t',
         autocommit=True
)

kursori = yhteys.cursor()

npcTypes = ["friendly", "robber", "player"]

tyypit = random.choice(npcTypes)
määrä = random.randint(1, 3)

kursori.execute(f"UPDATE airport SET npc_type = '{tyypit}' WHERE npc_type IS NULL;")

kursori.fetchall()

print("Time to play the game")
print("Press Enter to continue..")

player_name = input("Enter your name: ")

user_input = input()
if user_input == "":
    print("Choose your starting point")

kursori.execute("SELECT airport.name, iso_country FROM airport ORDER BY RAND() LIMIT 3")
tulos = (kursori.fetchall())

for x in tulos:
    index = tulos.index(x)
    print(f"{index + 1}. {x}")

dirk = 0
life = 0
bums = ["bum"]
bum = random.choice(bums)

airport_comment = [
    "During your exploration, you come upon a passage where a small group of bums can be seen; "
    "you decide to check it out.",
    "While navigating around the airport, you discover a hallway with a handful of bums, "
    "leading you to investigate further.",
    "As you move about, a corridor with a few bums becomes evident, compelling you to make your way there.",
    "In your journey, you stumble upon a passage where a few bums are present, prompting you to explore.",
    "While exploring the surroundings, you find a hallway with a small group of bums, "
    "and you decide to head in that direction.",
    "As you wander, a corridor filled with bums in need of a gambling catches your attention, "
    "urging you to approach.",
    "During your journey, you encounter a passage where a small group of bums can be observed; "
    "you decide to investigate.",
    "While navigating, you chance upon a hallway with a handful of bums, motivating you to explore further.",
    "As you stroll, a corridor featuring a few bums becomes visible, compelling you to make your way there.",
    "In your exploration, you happen upon a passage where a few bums are present, prompting you to investigate.",
    "As you walk around, a corridor occupied by bums in need of gambling captures your attention, "
    "urging you to approach.",
    "During your journey, you discover a passage where a small group of bums can be seen; you decide to check it out.",
    "While navigating around the airport, you notice a hallway with a handful of bums, "
    "motivating you to explore further.",
    "As you move about, a corridor with a few bums becomes evident, compelling you to make your way there.",
    "In your exploration, you stumble upon a passage where a few bums are present, prompting you to explore.",
    "While exploring the surroundings, you find a hallway with a small group of bums, "
    "and you decide to head in that direction.",
    "As you wander, a corridor filled with bums in need of gambling catches your attention, "
    "urging you to approach.",
    "During your journey, you encounter a passage where a small group of bums can be observed; "
    "you decide to investigate."
]
print_airport_comment = random.choice(airport_comment)

def random_airport():
    airports = [
        "Helsinkivantaa", "Rio de Janeiro"
    ]
    return random.choice(airports)

def bum_encounter(bum_count):
    global raha
    global dirk
    global life

    time.sleep(3)
    dialog_bum_encounter1 = [
        f"You have stumbled upon a wild {bum}.",
        f"A feral figure appears in your path, a {bum}.",
        f"In your way stands an untamed wanderer, a {bum}.",
        f"A rogue character emerges before you, a {bum}.",
        f"You find yourself face to face in the home turf of the {bum}.",
        f"Your travels are halted, you notice an uncontrolled street dweller, a {bum}.",
        f"A rogue individual appears in your presence, a {bum}."
    ]
    print_bum_encounter1 = random.choice(dialog_bum_encounter1)
    print(print_bum_encounter1)

    time.sleep(2)
    dialog_bum_encounter2 = [
        "Will you engage in a game with the bum, procure a knife from them, or attempt to extract information?",
        "Are you inclined to partake in a game with the bum, buy a knife, or seek information?",
        "Will you entertain the possibility of a game with the bum, making a knife purchase, "
        "or extracting information?",
        "Are you open to participating in a game with the bum, securing a knife, or obtaining information?",
        "Would you consider joining a game with the bum, procuring a knife, or attempting to gather information?",
        "Are you up for engaging in a game with the bum, buying a knife, or seeking information?",
        "Will you consider playing a game with the bum, purchasing a knife, or extracting information?",
        "Do you desire to participate in a game with the bum, obtain a knife, or try to gather information?"
    ]
    print_bum_encounter2 = random.choice(dialog_bum_encounter2)
    print(print_bum_encounter2)

    time.sleep(2)
    dialog_bum_encounter3 = [
        "Choose your action: ",
        "Decide what to do: ",
        "Pick your action: ",
        "Choose your next step: ",
        "Decide your course of action: ",
        "Select an option: ",
        "Opt for your action: ",
        "Decide your move: "
        ]
    print_bum_encounter3 = random.choice(dialog_bum_encounter3)
    print(print_bum_encounter3)

    dialog_action1 = [
        "Engage in a game. ",
        "Engage in a gaming session. ",
        "Participate in a game. ",
        "Participate in a gaming session. ",
        "Take part in a game. ",
        "Take part in a gaming session. ",
        "Indulge in some gaming. "
    ]
    print_action1 = random.choice(dialog_action1)
    dialog_action2 = [
        "Proceed with a transaction. ",
        "Conduct a buying activity. ",
        "Make a deal. ",
        "Make a transaction. ",
        "Commit purchasing activities. ",
        "Commit a deal. ",
        "Indulge in some purchasing activities. ",
        "Indulge in some dealing. "
        "Initiate a buying process. ",
        "Initiate a purchase. ",
        "Initiate in some purchasing activities. ",
        "Initiate a buying activity. "
    ]
    print_action2 = random.choice(dialog_action2)
    dialog_action3 = [
        "Inquire for details on TheBauss. ",
        "Inquire for information. ",
        "Inquire for knowledge. ",
        "Seek information. ",
        "Seek insights. ",
        "Seek knowledge. ",
        "Ask for insights. ",
        "Ask for knowledge. ",
        "Ask for information. ",
        "Request information. ",
        "Gather intel. ",
        "Kindly request information. ",
        "Pose a query. ",
        "Solicit information. ",
        "Probe for details. ",
        "Request insights. ",
        "Inquire for knowledge. "
    ]
    print_action3 = random.choice(dialog_action3)
    dialog_action4 = [
        "Continue your journey. ",
        "Keep moving forward. ",
        "Proceed on your path. ",
        "Move along. ",
        "Walk on. ",
        "Keep walking. "
    ]
    print_action4 = random.choice(dialog_action4)
    action = input("\n1. " + print_action1 +
                   "\n2. " + print_action2 +
                   "\n3. " + print_action3 +
                   "\n4. " + print_action4 + "\n")

    if action == "1":
        play_game(bum_count)
    elif action == "2":
        purchase_knife(bum_count)
    elif action == "3":
        request_information(bum_count)
    elif action == "4":
        print("You continued on your way. ")
        bum_count -= 1
        return bum_count
    else:
        print("Invalid input, encounter will now end. Better luck next time.")
    bum_count -= 1
    return bum_count

def play_game(bum_count):
    print("mustajaakko ei löytyny")
    # laitetaan tähän mustajaakko
    bum_count -= 1
    return bum_count
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    bet = 1

    def jako(deck):
        käsi = []
        for i in range(2):
            random.shuffle(deck)
            kortti = random.choice(deck)
            if kortti == 11: kortti = "J"
            if kortti == 12: kortti = "Q"
            if kortti == 13: kortti = "K"
            if kortti == 14: kortti = "A"
            käsi.append(kortti)
        return käsi

    def total(käsi):
        total = 0
        for kortti in käsi:
            if kortti == "J" or kortti == "Q" or kortti == "K":
                total += 10
            elif kortti == "A":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += int(kortti)  # Convert the card string to an integer
        return total

    def play_again():
        again = input("Do you want to play again Y/N?").lower()
        if again == "y":
            dealer_käsi = []
            player_käsi = []
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
            game()
        else:
            print("Thanks for playing!")
            exit()

    def hit():
        kortti = deck.pop()
        if kortti == 11:
            kortti = "J"
        if kortti == 12:
            kortti = "Q"
        if kortti == 13:
            kortti = "K"
        if kortti == 14:
            kortti = "A"
        käsi.append(kortti)
        return käsi

    def print_result(dealer_käsi, player_käsi):
        clear()

        print("Time to play blackjack")
        print("Dealer has a " + str(dealer_käsi) + "for a total of " + str(total(dealer_käsi)))
        print("Player has a" + str(player_käsi) + "for a total of " + str(total(player_käsi)))

    def blackjack(dealer_käsi, player_käsi):
        if total(player_käsi) == 21:
            print_result(player_käsi, dealer_käsi)
            print("You got a blackjack!")
        elif total(dealer_käsi) == 21:
            print_result(dealer_käsi, player_käsi)
            print("The dealer has a blackjack")
            raha -= bet

    def score(dealer_käsi, player_käsi):
        if total(player_käsi) == 21:
            print_result(dealer_käsi, player_käsi)
            print("You got a blackjack!")
        elif total(dealer_käsi) == 21:
            print_result(dealer_käsi, player_käsi)
            print("The dealer has a blackjack")
        elif total(player_käsi) > 21:
            print_result(dealer_käsi, player_käsi)
            print("You bust")
        elif total(dealer_käsi) > 21:
            print_result(dealer_käsi, player_käsi)
            print("The dealer busts")
            raha += bet * 1.5
        elif total(player_käsi) < total(dealer_käsi):
            print_result(dealer_käsi, player_käsi)
            print("The dealer has a higher score")
            raha -= bet
        elif total(player_käsi) > total(dealer_käsi):
            print_result(dealer_käsi, player_käsi)
            print("You have a higher score")
            raha += bet * 1.5
        elif total(player_käsi) == total(dealer_käsi):
            print_result(dealer_käsi, player_käsi)
            print("It's a tie")
            raha -= bet

    def make_bet():
        global bet
        bet = 0
        print("How much would you like to bet")
        while bet == 0:
            bet_comp = input()
            bet_comp = int(bet_comp)

            if bet_comp >= 1 and bet_comp <= raha:
                bet = bet_comp
            else:
                print("You only have " + str(raha))

    def game():
        choice = 0
        print("Time to game")
        dealer_käsi = jako(deck)
        player_käsi = jako(deck)
        print("dealer has " + str(dealer_käsi[0]))
        make_bet()
        print("You have a " + str(player_käsi[0]))
        blackjack(dealer_käsi, player_käsi)
        quit = False
        while not quit:
            choice = input("Do you want to [H]it, [S]tand or [Q]uit").lower()
            if choice == 'h':
                hit(player_käsi)
                if total(player_käsi) > 21:
                    print("You bust")
                    raha -= bet
                    play_again()
                elif choice == 's':
                    while total(dealer_käsi) < 17:
                        hit(dealer_käsi)
                        print(dealer_käsi)
                        if total(dealer_käsi) > 21:
                            print("Dealer busts")
                            raha += bet * 1.5
                            play_again()
                        score(dealer_käsi, player_käsi)
                        play_again()
                elif choice == 'q':
                    print("Thanks for the game")
                    quit = True
                    exit()


def purchase_knife(bum_count):
    global raha
    global dirk
    global bum

    knife_buy = input(f"{bum}: So you wish to purchase a knife huh? \nInput yes / no\n")
    if knife_buy == 'yes':
        acquire_a_shank = input(f"{bum}: You can have it for 300. \nInput yes / no\n")
        if acquire_a_shank == 'yes':
            print("shank acquired")
            raha -= 300
            dirk = 1
            time.sleep(1)
            print(f"{bum}: A favorable deal")
            time.sleep(1)
            print("Bum takes off and disappears to the crowds. ")
            time.sleep(2)
            return bum_count
        elif acquire_a_shank == 'no':
            print(f"{bum}: Stop bothering me then??")
            time.sleep(1)
            print("Bum takes off and disappears to the crowds. ")
            time.sleep(2)
            bum_count -= 1
            return bum_count
        else:
            print("Invalid input, encounter will now end. Better luck next time.")
            bum_count -= 1
            return bum_count
    elif knife_buy == 'no':
        print(f"{bum}: Stop bothering me then??")
        bum_count -= 1
        return bum_count
    else:
        print("Invalid input, encounter will now end. Better luck next time.")
        bum_count -= 1
        return bum_count


def request_information(bum_count):
    global raha
    global dirk
    global life

    inforequest = [1, 2, 3, 4]
    inforequest_outcome = random.choice(inforequest)
    if inforequest_outcome == 1:
        print("The less fortunate individual extends an invitation, "
              "challenging you to engage in a refined fencing duel. ")
        time.sleep(3)
        if dirk == 1:
            print("You pull your knife out.")
            time.sleep(1)
            print("The bum notices the knife and decides to exit the fencing duel by running away.")
            time.sleep(2)
        else:
            print("The call to join was not voluntary and the bum charges towards you")
            time.sleep(2)
            time.sleep(1)
            bumcharge_outcome = random.randint(1, 3)
            if bumcharge_outcome == 1:
                print("With agile finesse, you skillfully evaded the oncoming advance of the bum, "
                      "escaping their charge, and gracefully exited the scene, "
                      "leaving the duel behind")
                time.sleep(4)
            else:
                dialog_death = [
                    "After an agile maneuver, the bum successfully struck, leaving me wounded and bleeding.",
                    "A quick and nimble move from the bum resulted in a successful hit, leaving you wounded.",
                    "Executing a swift and nimble move, the bum landed a successful strike, leaving you injured.",
                    "The bum executed a swift maneuver, landing a successful hit that left you wounded.",
                    "A nimble move from the bum resulted in a successful strike, leaving you injured and bleeding.",
                    "Executing a swift maneuver, the homeless bum landed a hit, leaving you wounded and bleeding.",
                    "A speedy move from the bum resulted in a successful strike, leaving you injured and bleeding.",
                    "A nimble maneuver from the homeless bum resulted in a successful hit, leaving you wounded.",
                    "With a quick move, the bum executed a hit, causing you to be injured and bleeding.",
                    "A rapid maneuver from the bum led to a successful strike, leaving you wounded and bleeding.",
                    "Following a swift move by the bum, a precise strike ensued, resulting in you being injured.",
                    "After a quick maneuver by the bum, they executed a hit, causing you to be wounded.",
                    "After a nimble maneuver by the bum, they executed a hit, leaving you wounded and bleeding.",
                    "Following a rapid maneuver by the bum, a successful hit ensued, resulting in you being wounded.",
                    "Executing a speedy move, the bum landed a hit, resulting in you being injured and bleeding.",
                    "In the wake of a swift move by the homeless bum, they struck, leaving you injured and bleeding.",
                    "In the aftermath of a rapid move by the homeless bum, they struck, causing you to be injured.",
                    "In the wake of a quick maneuver by the bum, they struck, causing you to be wounded and bleeding.",
                    "In the aftermath of a nimble maneuver by the homeless bum, they struck, leaving you wounded and.",
                    "In the wake of a nimble move by the homeless bum, they struck, causing you to be bleeding."
                ]
                print_death = random.choice(dialog_death)
                print(print_death)
                time.sleep(4)
                print("You Died. ")
                life = 1
    elif inforequest_outcome == 2:
        print(f"{bum}: I am no snitch. ")
        print(f"{bum} walks away. ")
        bum_count -= 1
        return bum_count
    else:
        info_buy = input(f"{bum}: I can sell you a clue for 100. \nInput yes / no\n")
        if info_buy == 'yes':
            raha -= 100
            print("clue")
        elif info_buy == 'no':
            print(f"{bum}: Stop bothering me then??")
            time.sleep(1)
            print(f"{bum} takes off and disappears to the crowds. ")
            bum_count -= 1
            return bum_count
        else:
            print("Invalid input, encounter will now end. Better luck next time. ")
            bum_count -= 1
            return bum_count

def beginning():
    print("Game ✧ Start")
    print("Your objective: \nFind TheBausses lair and them "
          "\nvia purchasing information from various bums you encounter on your travels."
          "\nBeat TheBauss because they are very bad for the climate. ")

def airport_visit():
    print(f"You start from {random_airport()} the airport."
          "\nThere are a lot of people here. ")
    time.sleep(1)
    print(print_airport_comment)

    bum_count = int(random.randint(3, 5))
    while bum_count > 0:
        bum_count = bum_encounter(bum_count)


def airport_arrive():
    print(f"You arrive to {random_airport()} the airport."
          "\nThere are a lot of people here. ")
    time.sleep(1)
    print(print_airport_comment)

    bum_count = int(random.randint(3, 5))
    while bum_count > 0:
        bum_count = bum_encounter(bum_count)

start = input("Type in number (1-3) and press Enter to continue..")

def startingPoint(start):
    valinta = tulos[int(start) - 1]
    kursori.execute("INSERT INTO game (location) VALUES (%s), (%s);", (valinta))
    print(f"U start at the airport {valinta}")
    print("Have fun)")
    return valinta

startingPoint(start)
def robbery():
    chance = 0.75
    arpa = float(random.randint(0, 1))

    if arpa > chance:
        print("Local is willing to rob u, can u protect urself?")
        syöte = input("Press 'K' to use a knife ")

        if syöte == "K":
            kursori.execute("SELECT Knife FROM inventory")
            puukko = kursori.fetchone()

            if puukko[0] > 0:
                print("U pull out ur knife and threaten robber with it, he walks away.. Press Enter to continue..")
                kursori.execute("UPDATE inventory SET Knife = Knife - 1 WHERE Knife > 0")
        else:
            kursori.execute("UPDATE inventory SET money = money * 0.5")

            kursori.execute("SELECT money FROM inventory")
            rahaTilanne = kursori.fetchone()[0]

            print("Damn it, I didn't have my knife with me..")
            print("Luckily I always hide half of my money in my socks")
            print(f"Well.. now I have {rahaTilanne} ")
    else:
        chooseNpc()

    return
class Player:
    pass

class Friendly:
    def tryToBuyCode(self):
        print("U know anything about THE CODE? ")
        # ei midii hajuu viel

listOfNpc = [Friendly,Player]

def chooseNpc():

    npc = random.choice(listOfNpc)

    if npc == Friendly:
        olio = Friendly
        print("U meet friendly npc and have dialogue")
        #dialogue metodi

    elif npc == Player:
        Olio = Player
        print("U've met local card player, down to play?")
        #metodi card game
    return npc

def arrival():
    print(f"U see {random.randint(1,3)} people")
    print("Which one do u want to talk to?")
    valinta = input("Type in number (1-3) and press Enter to continue..")

    if valinta == "1" or valinta == "2" or valinta == "3":
        chooseNpc()
    return

arrival()

#boss fight
def play_russian_roulette():
    print('"Welcome to Bausses lair!"')
    print("\"I like to play with high stakes..so let's play some Russian Roulette HAHA!\"")
    print("You start by pulling the trigger.")

    chambers = 6
    bullet_chamber = random.randint(1, chambers)

    while True:
        input("Your turn, press enter to pull the trigger! ")

        if chambers == bullet_chamber:
            print("BANG! You lose!")
            print("Game over")
            time.sleep(1)
            break
        else:
            print("Click! You live that one.")
            chambers -= 1

        if chambers == 1:
            print("Click! You survived! You know the boss will have to admit defeat now.")
            time.sleep(1)
            print("Well after all this, I am an honorable man.")
            time.sleep(1)
            print("BANG! TheBaus pulls the trigger on himself")
            time.sleep(1)
            print("You win! Congratulations!")
            time.sleep(1)
            print("Well played! Game over.")
            time.sleep(1)
            break

        print("Bausses turn")
        time.sleep(1)
        print('"You ready for your demice?"')
        time.sleep(1)


        if chambers == bullet_chamber:
            print("BANG! TheBaus loses!")
            time.sleep(1)
            break
        else:
            print("*The boss pulls the trigger")
            time.sleep(1)
            print("Click! The boss lives that one.")
            chambers -= 1