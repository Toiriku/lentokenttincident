import os
import random
import time
import string
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='demogame',
         user='root',
         password='bamse',
         autocommit=True
)

kursori = yhteys.cursor()


raha = 100000
dirk = 0
life = 0
bum_count = 0
code_collected = []
bums = [
    "unfortunate individual",
    "street dweller",
    "beggar",
    "esteemed companion",
    "exquisite street dweller",
    "street connoisseur",
    "great financial decision maker",
    "untamed wanderer",
    "wild bum"
]
eri_ending = [
    "time to ",
    "it's time to ",
    "let's "
]
eri_ender = [
    "relocate. ",
    "go elsewhere. ",
    "move on. ",
    "find a new location. "
]
pummit_loppu = [
    f"This area contains no more {random.choice(bums)}s, {random.choice(eri_ending)}{random.choice(eri_ender)}",
    f"This location contains no more {random.choice(bums)}s, {random.choice(eri_ending)}{random.choice(eri_ender)}",
    f"This place contains no more {random.choice(bums)}s, {random.choice(eri_ending)}{random.choice(eri_ender)}",

    f"There are no more {random.choice(bums)}s in this area, {random.choice(eri_ending)}{random.choice(eri_ender)}",
    f"There are no more {random.choice(bums)}s in this location, {random.choice(eri_ending)}{random.choice(eri_ender)}",
    f"There are no more {random.choice(bums)}s in this place, {random.choice(eri_ending)}{random.choice(eri_ender)}",

    f"You see no more {random.choice(bums)}s in this location, {random.choice(eri_ending)}{random.choice(eri_ender)}",
    f"You see no more {random.choice(bums)}s in this place, {random.choice(eri_ending)}{random.choice(eri_ender)}",
    f"You see no more {random.choice(bums)}s in here, {random.choice(eri_ending)}{random.choice(eri_ender)}"

]
airport_comment = [
    f"During your exploration, you come upon a passage where a small group of {random.choice(bums)}s can be seen; "
    "you decide to check it out.",
    f"While navigating around the airport, you discover a hallway with a handful of {random.choice(bums)}s, "
    "leading you to investigate further.",
    f"As you move about, a corridor with a few {random.choice(bums)}s becomes evident, compelling you to make your way there.",
    f"In your journey, you stumble upon a passage where a few {random.choice(bums)}s are present, prompting you to explore.",
    f"While exploring the surroundings, you find a hallway with a small group of {random.choice(bums)}s, "
    "and you decide to head in that direction.",
    f"As you wander, a corridor filled with {random.choice(bums)}s in need of a gambling catches your attention, "
    "urging you to approach.",
    f"During your journey, you encounter a passage where a small group of {random.choice(bums)}s can be observed; "
    "you decide to investigate.",
    f"While navigating, you chance upon a hallway with a handful of {random.choice(bums)}s, motivating you to explore further.",
    f"As you stroll, a corridor featuring a few {random.choice(bums)}s becomes visible, compelling you to make your way there.",
    f"In your exploration, you happen upon a passage where a few {random.choice(bums)}s are present, prompting you to investigate.",
    f"As you walk around, a corridor occupied by {random.choice(bums)}s in need of gambling captures your attention, "
    "urging you to approach.",
    f"During your journey, you discover a passage where a small group of {random.choice(bums)}s can be seen; you decide to check it out.",
    f"While navigating around the airport, you notice a hallway with a handful of {random.choice(bums)}s, "
    "motivating you to explore further.",
    f"As you move about, a corridor with a few {random.choice(bums)}s becomes evident, compelling you to make your way there.",
    f"In your exploration, you stumble upon a passage where a few {random.choice(bums)}s are present, prompting you to explore.",
    f"While exploring the surroundings, you find a hallway with a small group of {random.choice(bums)}s, "
    "and you decide to head in that direction.",
    f"As you wander, a corridor filled with {random.choice(bums)}s in need of gambling catches your attention, "
    "urging you to approach.",
    f"During your journey, you encounter a passage where a small group of {random.choice(bums)}s can be observed; "
    "you decide to investigate."
]
print_airport_comment = random.choice(airport_comment)
travel_dialogue = ["Where will u go?",
                    "Where are u planning to go?",
                    "Where are u planning to go?",
                    "Where shall u go?"]

def bum_encounter():
    global raha, dirk, life, bum_count
    bum_count -= 1
    time.sleep(3)
    dialog_bum_encounter1 = [
        f"You have stumbled upon a {random.choice(bums)}.",
        f"A feral figure appears in your path, a {random.choice(bums)}.",
        f"In your way stands an untamed wanderer, a {random.choice(bums)}.",
        f"A rogue character emerges before you, a {random.choice(bums)}.",
        f"You find yourself face to face in the home turf of the {random.choice(bums)}.",
        f"Your travels are halted, you notice a {random.choice(bums)}.",
        f"A rogue individual appears in your presence, a {random.choice(bums)}."
    ]
    print_bum_encounter1 = random.choice(dialog_bum_encounter1)
    print(print_bum_encounter1)

    time.sleep(2)
    dialog_bum_encounter2 = [
        f"Will you engage in a game with the {random.choice(bums)}, procure a knife from them, or attempt to extract information?",
        f"Are you inclined to partake in a game with the {random.choice(bums)}, buy a knife, or seek information?",
        f"Will you entertain the possibility of a game with the {random.choice(bums)}, making a knife purchase, "
        "or extracting information?",
        f"Are you open to participating in a game with the {random.choice(bums)}, securing a knife, or obtaining information?",
        f"Would you consider joining a game with the {random.choice(bums)}, procuring a knife, or attempting to gather information?",
        f"Are you up for engaging in a game with the {random.choice(bums)}, buying a knife, or seeking information?",
        f"Will you consider playing a game with the {random.choice(bums)}, purchasing a knife, or extracting information?",
        f"Do you desire to participate in a game with the {random.choice(bums)}, obtain a knife, or try to gather information?"
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
        "Inquire for details on Taylor Swifts location. ",
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
        play_game()
    elif action == "2":
        purchase_knife()
    elif action == "3":
        request_information()
    elif action == "4":
        print("You continued on your way. ")
    elif action == "boss":
        accept_boss_challenge()
    else:
        print("Invalid input, encounter will now end. Better luck next time.")

def purchase_knife():
    global raha, dirk, bum

    knife_buy = input(f"{random.choice(bums)}: So you wish to purchase a knife huh? \nInput yes / no\n")
    if knife_buy == 'yes':
        acquire_a_shank = input(f"{random.choice(bums)}: You can have it for 300. \nInput yes / no\n")
        if acquire_a_shank == 'yes':
            print("shank acquired")
            raha -= 300
            dirk = 1
            time.sleep(1)
            print(f"{random.choice(bums)}: A favorable deal")
            time.sleep(1)
            print(f"{random.choice(bums)} takes off and disappears to the crowds. ")
            time.sleep(2)
        elif acquire_a_shank == 'no':
            print(f"{random.choice(bums)}: Stop bothering me then??")
            time.sleep(1)
            print(f"{random.choice(bums)} takes off and disappears to the crowds. ")
            time.sleep(2)
        else:
            print("Invalid input, encounter will now end. Better luck next time.")
    elif knife_buy == 'no':
        print(f"{random.choice(bums)}: Stop bothering me then??")
    else:
        print("Invalid input, encounter will now end. Better luck next time.")

def request_information():
    global code_collected, code, raha, dirk, life

    inforequest = random.randint(1, 4)

    if inforequest == 1:
        print(f"The {random.choice(bums)} extends an invitation, "
              "challenging you to engage in a refined fencing duel. ")
        time.sleep(3)
        if dirk == 1:
            print("You pull your knife out.")
            time.sleep(1)
            print(f"The {random.choice(bums)} notices the knife and decides to exit the fencing duel by running away.")
            time.sleep(2)
        else:
            print(f"The call to join was not voluntary and the {random.choice(bums)} charges towards you")
            time.sleep(2)
            bumcharge_outcome = random.randint(1, 3)
            if bumcharge_outcome == 1:
                print(f"With agile finesse, you skillfully evaded the oncoming advance of the {random.choice(bums)}, "
                      "escaping their charge, and gracefully exited the scene, "
                      "leaving the duel behind")
                time.sleep(4)
            else:
                dialog_death = [
                    f"After an agile maneuver, the {random.choice(bums)} successfully struck, leaving me wounded and bleeding.",
                    f"A quick and nimble move from the {random.choice(bums)} resulted in a successful hit, leaving you wounded.",
                    f"Executing a swift and nimble move, the {random.choice(bums)} landed a successful strike, leaving you injured.",
                    f"The {random.choice(bums)} executed a swift maneuver, landing a successful hit that left you wounded.",
                    f"A nimble move from the {random.choice(bums)} resulted in a successful strike, leaving you injured and bleeding.",
                    f"Executing a swift maneuver, the {random.choice(bums)} landed a hit, leaving you wounded and bleeding.",
                    f"A speedy move from the {random.choice(bums)} resulted in a successful strike, leaving you injured and bleeding.",
                    f"A nimble maneuver from the {random.choice(bums)} resulted in a successful hit, leaving you wounded.",
                    f"With a quick move, the {random.choice(bums)} executed a hit, causing you to be injured and bleeding.",
                    f"A rapid maneuver from the {random.choice(bums)} led to a successful strike, leaving you wounded and bleeding.",
                    f"Following a swift move by the {random.choice(bums)}, a precise strike ensued, resulting in you being injured.",
                    f"After a quick maneuver by the {random.choice(bums)}, they executed a hit, causing you to be wounded.",
                    f"After a nimble maneuver by the {random.choice(bums)}, they executed a hit, leaving you wounded and bleeding.",
                    f"Following a rapid maneuver by the {random.choice(bums)}, a successful hit ensued, resulting in you being wounded.",
                    f"Executing a speedy move, the {random.choice(bums)} landed a hit, resulting in you being injured and bleeding.",
                    f"In the wake of a swift move by the {random.choice(bums)}, they struck, leaving you injured and bleeding.",
                    f"In the aftermath of a rapid move by the {random.choice(bums)}, they struck, causing you to be injured.",
                    f"In the wake of a quick maneuver by the {random.choice(bums)}, they struck, causing you to be wounded and bleeding.",
                    f"In the aftermath of a nimble maneuver by the {random.choice(bums)}, they struck, leaving you wounded and.",
                    f"In the wake of a nimble move by the {random.choice(bums)}, they struck, causing you to be bleeding."
                ]
                print_death = random.choice(dialog_death)
                print(print_death)
                time.sleep(4)
                print("You Died. ")
                life = 1
                exit()

    elif inforequest == 2:
        print(f"{random.choice(bums)}: I am no snitch. ")
        print(f"{random.choice(bums)} disappears. ")

    else:
        info_buy = input(f"{random.choice(bums)}: I can sell you a clue for 500. \nInput yes / no\n")
        if info_buy == 'yes':
            raha -= 500
            clue = random.choice(code)
            print("Bum pulls out piece of paper with something written on it ")
            print(f"The {random.choice(bums)} pulls out piece of paper with something written on it ")
            print("He quickly hands you the paper and disappears while you are carefully unfolding it ")
            print(f"'{clue}' is written on the paper")
            if clue not in code_collected:
                print(random.choice(code_dialogues1))
                code_collected.append(clue)
                print("Code collected:", code_collected)
                if code_collected == code:
                    print("Seems like you finally have everything u needed to get to her..")
                    accept_boss_challenge()
            else:
                print(random.choice(code_dialogues2))

def accept_boss_challenge():
    global code_collected, code, life
    if code_collected == code:
        haaste = input("Are you ready to challenge Taylor 'The Final Boss' Swift ? \nInput yes / no\n")
        if haaste == "yes":
            if raha >= 2000:
                boss_tasolle = input("You seem fit to start the final duel, are you sure that you want to continue? \nInput yes / no\n")
                if boss_tasolle == "yes":
                    play_russian_roulette()
                elif boss_tasolle == "no":
                    print("Hahaha you are a bloody coward..")
                    travel()
            else:
                print("You need to have at least '2000' to play with her, you can't play with her")
                travel()
        elif haaste == "no":
            print("What a coward..")
            travel()
    else:
        print("You don't have all the necessary pieces of code yet.")

def codeCreation():
    global code, code_collected
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choices(characters, k=1))
    if code_collected == code:
        accept_boss_challenge()
    return code

code_dialogues1 = ["You got piece of code you needed",
                   "You are one step closer to that devil..",
                   "That is exactly what you needed",
                   "That clue will help u get to the boss..",
                   ]
code_dialogues2 = ["U already have that one, damn it ..",
                   "Not the one u needed.."
                   f"{random.choice(bums)} sold u some crap, u got scammed"
                   "That piece of paper has nothing to do with the boss, better luck next time!"]
codeCreation()

def play_game():
    game()
    return
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
bet = 1

def shuffle():
    random.shuffle(deck)

def nosto():
    kortti = deck.pop(0)
    if kortti == 11:
        kortti = "J"
    elif kortti == 12:
        kortti = "Q"
    elif kortti == 13:
        kortti = "K"
    elif kortti == 14:
        kortti = "A"
    return kortti

def total(kasi):
    total_value = 0
    num_aces = 0
    for kortti in kasi:
        if isinstance(kortti, int):
            total_value += kortti
            if kortti == 11:
                num_aces += 1
        elif kortti == "J" or kortti == "Q" or kortti == "K":
            total_value += 10
        elif kortti == "A":
            num_aces += 1
            total_value += 11

    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1
    return total_value

def print_result(dealer_kasi, player_kasi):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("dealer has: ", dealer_kasi, " (total", total(dealer_kasi), ")")
    print("player has: ", player_kasi, " (total", total(player_kasi), ")")

def game():
    global raha, bet, dealer_kasi, player_kasi
    shuffle()
    dealer_kasi = []
    player_kasi = []
    print("Its time to play Blackjack")
    make_bet()
    dealer_kasi.append(nosto())
    player_kasi.append(nosto())
    player_kasi.append(nosto())
    print_result(dealer_kasi, player_kasi)

    while True:
        choice = input("Would you like to [H]it or [S]tand").lower()
        if choice == 'h':
            player_kasi.append(nosto())
            print_result(dealer_kasi, player_kasi)
            if total(player_kasi) > 21:
                print("You bust")
                print(f"You only have {raha} amount of money lol")
                break
        elif choice == 's':
            while total(dealer_kasi) < 17:
                dealer_kasi.append(nosto())
                print("Dealer hits: ", dealer_kasi)
            score(dealer_kasi, player_kasi)
            break

def score(dealer_kasi, player_kasi):
    global raha
    dealer_total = total(dealer_kasi)
    player_total = total(player_kasi)
    if player_total == 21:
        raha += bet * 2.5
        print(f"Your total is: {raha}")
    if player_total > 21:
        print("You bust! Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busts! You win.")
        raha += bet * 2.5
    elif player_total > dealer_total:
        print("You win!")
        raha += bet * 2.5
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a tie.")
        raha += bet
    print("Your remaining money:", raha)
    bum_encounter()

def make_bet():
    global bet, raha
    print("You have", raha)
    while True:
        bet_amount = input("How much would you like to bet? ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount <= raha:
                bet = bet_amount
                raha -= bet
                break
            else:
                print("You don't have enough money!")
        else:
            print("Please enter a valid bet amount.")

def beginning():
    print("Game ✧ Start")
    time.sleep(1)
    print("Your objective: \nFind Taylor Swifts lair and them "
          f"\nvia purchasing information from various {random.choice(bums)}s you encounter on your travels."
          "\nBeat Taylor Swift because she is very bad for the climate. ")
    time.sleep(4)

def travel():
    global bum_count
    print(random.choice(travel_dialogue))
    time.sleep(2)
    print()
    kentat = "SELECT name, continent FROM airport ORDER BY RAND() LIMIT 3"
    kursori.execute(kentat)
    options = kursori.fetchall()
    for index, x in enumerate(options):
        print(f"{index +1}. {x[0]} {x[1]}")
    print()
    valinta = int(input("Choose 1, 2, or 3 and press Enter to continue.."))

    while valinta not in (1, 2, 3):
        print("Invalid input ")
        valinta = int(input("Choose 1, 2, or 3 and press Enter to continue.."))
    else:
        selected_location = options[valinta - 1][0]
        kursori.execute("UPDATE game SET location = %s", (selected_location,))
        kursori.execute("SELECT location FROM game")
        sijainti = kursori.fetchone()
        print(f"You arrive at {sijainti[0]}")

    kursori.fetchall()

    bum_count += 3
    return

#boss fight
def play_russian_roulette():
    print('"Welcome to Swifts lair!"')
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
            exit()
        else:
            print("Click! You live that one.")
            chambers -= 1

        if chambers == 1:
            print("Click! You survived! You know Taylor will have to admit defeat now.")
            time.sleep(1)
            print("Well after all this, I am an honorable woman.")
            time.sleep(1)
            print("BANG! Taylor pulls the trigger on herself")
            time.sleep(1)
            print("You win! Congratulations!")
            time.sleep(1)
            print("Well played! Game over.")
            time.sleep(1)
            exit()

        print("Taylor's turn")
        time.sleep(1)
        print("You ready for your demice?")
        time.sleep(1)


        if chambers == bullet_chamber:
            print("BANG! Swift sucks!")
            time.sleep(1)
            exit()

        else:
            print("*Taylor pulls the trigger")
            time.sleep(1)
            print("Click! Taylor lives that one. :( ")
            chambers -= 1

def accept_boss_challenge():
    haaste = input("Are you ready to challenge Taylor 'The Final Boss' Swift ? \nInput yes / no\n")
    if haaste == "yes":
        if raha > 1999:
            boss_tasolle = input("U seem to be fit to start the final game, are you sure that you want to continue? \nInput yes / no\n")
            if boss_tasolle == "yes":
                play_russian_roulette()
            elif boss_tasolle == "no":
                print("Hahaha you are a bloody coward..")
                travel()
        else:
            print("U need to have at least '2000' to play with her, you can't play with her")
            travel()
    if haaste == "no":
        print("What a coward..")
        travel()

def peli():
    beginning()
    while life == 0:
        while bum_count == 0:
            travel()
            while bum_count > 0:
                bum_encounter()
peli()
