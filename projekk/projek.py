"""
import os, string
"""
import random
import mysql.connector
from flask import Flask
from flask import render_template, request

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='demogame',
         user='root',
         password='liikeonlääke',
         autocommit=True
)

app = Flask(__name__)

kursori = yhteys.cursor()

bums = ["bum"]
bum = random.choice(bums)

travel_dialogue = ["Where will u go next ?",
                    "Where are u planning to go now?",
                    "Where are u planning to go next?",
                    "Where shall u go now ?"]

class Inventory:
    def __init__(self, raha, dirk):
        self.raha = int(raha)
        self.dirk = int(dirk)

    def map(self):
        return {"raha":  str(self.raha), "dirk": str(self.dirk)}

def bum_encounter(content=None, inventory=None):
    if content is None:
        content = []
    if inventory is None:
        inventory = Inventory(0, 0)
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
    content.append(print_bum_encounter1)

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
    content.append(print_bum_encounter2)

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
    content.append(print_bum_encounter3)

    dialog_action1 = [
        "Engage in a game. ",
        "Engage in a gaming session. ",
        "Participate in a game. ",
        "Participate in a gaming session. ",
        "Take part in a game. ",
        "Take part in a gaming session. ",
        "Indulge in some gaming. "
    ]
    content.append(f'1. {random.choice(dialog_action1)}')
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
    content.append(f'2. {random.choice(dialog_action2)}')
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
    content.append(f'3. {random.choice(dialog_action3)}')
    dialog_action4 = [
        "Continue your journey. ",
        "Keep moving forward. ",
        "Proceed on your path. ",
        "Move along. ",
        "Walk on. ",
        "Keep walking. "
    ]
    content.append(f'4. {random.choice(dialog_action4)}')
    return render_template("base.html", content=content, nappi1="1", nappi2="2", nappi3="3", nappi4="4", inventory=inventory.map(), action="bum_encounter")

@app.route("/bum_encounter", methods=["POST"])
def hello_bum_encounter():
    action = request.form["teko"]
    inventory = Inventory(request.form["raha"], request.form["dirk"])
    if action == "1":
        return play_game([], inventory)
    elif action == "2":
        return purchase_knife([], inventory)
    elif action == "3":
        print("ok")
    elif action == "4":
        content = ["You continued on your way. "]
        return travel(content, Inventory(request.form["raha"], request.form["dirk"]))
    return -1

def play_game(content, inventory):
    content.append("Arvaa minkä numeron heität 1-6")
    return render_template("base.html", content=content, nappi1="1", nappi2="2", nappi3="3", nappi4="4", nappi5="5", nappi6="6", inventory=inventory.map(), action="play_game")

@app.route("/play_game", methods=["POST"])
def actual_play_game():
    nopat = random.randint(1, 6)
    content = ["Heitit nopan"]
    inventory = Inventory(request.form["raha"], request.form["dirk"])
    if str(nopat) == request.form["teko"]:
        inventory.raha += 500
        content.append("Voitit pelin")
    else:
        inventory.raha -= 50
        content.append(f"Tulos oli {nopat}. Hävisit pelin.")
    return travel(content, inventory)


def purchase_knife(content=None, inventory=None, raha=0, dirk=0):
    if content is None:
        content = []
    if inventory is None:
        inventory = Inventory(0, 0)
    content.append('Do you wish to purchase a dirk knife?')
    return render_template("base.html", content=content, nappi1="yes", nappi2="no", raha=raha, action='purchase_knife')

@app.route("/purchase_knife", methods=["POST"])
def actual_purchase_knife():
    action = request.form["teko"]
    inventory = Inventory(request.form["raha"], request.form["dirk"])
    content = ["Dirk costs 300"]
    if action == "yes":
        inventory.dirk += 1
        inventory.raha -= 300
        content = ['You have purchased a knife']
    if action == "no":
        content = ['I guess not']
    return bum_encounter(content, inventory)

@app.route("/", methods=["GET"])
def travel(content=None, inventory=None):
    if content is None:
        content = []
    if inventory is None:
        inventory = Inventory(1000, 0)
    kentat = "SELECT name, continent FROM airport ORDER BY RAND() LIMIT 3"
    kursori.execute(kentat)
    options = kursori.fetchall()
    content.append(random.choice(travel_dialogue))
    content.append("Choose 1: ")
    print(inventory.raha)
    return render_template("base.html", content=content, nappi1=options[0], nappi2=options[1], nappi3=options[2], inventory=inventory.map(), action='travel')

@app.route("/travel", methods=["GET", "POST"])
def actual_travel():
    valinta = request.form["teko"]
    valinta = get_name(valinta)
    content = [f"U are at {valinta}"]
    inventory = Inventory(request.form["raha"], request.form["dirk"])
    print("Hello")
    return bum_encounter(content, inventory)

def get_name(roskaa):
    return roskaa.split("'")[1]


app.run()



"""

bum_count = 0

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

@app.route("/", methods=["GET", "POST"])
def purchase_knife(content=None, raha=0, dirk=0):
    if content is None:
        content = []
    content.append('Do you wish to purchase a dirk knife?')
    return render_template("base.html", content=content, nappi1="yes", nappi2="no", raha=raha, action='purchase_knife')


@app.route("/purchase_knife", methods=["POST"])
def actual_purchase_knife():
    action = request.form["teko"]
    if action == "yes":
        dirk+=1
    if action == "no":
        content=['I guess not']
    return



def codeCreation():
    global code_collected
    global code
    code_collected = []
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choices(characters, k=6))
    return code

code_dialogues1 = ["You got piece of code you needed",
                   "You are one step closer to that devil..",
                   "That is exactly what you needed",
                   "That clue will help u get to the boss..",
                   ]

code_dialogues2 = ["U already have that one, damn it ..",
                   "Not the one u needed.."
                   "Bum sold u some crap, u got scammed"
                   "That piece of paper has nothing to do with the boss, better luck next time!"]



codeCreation()

def request_information():
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
        return

    else:
        info_buy = input(f"{bum}: I can sell you a clue for 500. \nInput yes / no\n")
        if info_buy == 'yes':
            raha -= 500
            clue = random.choice(code)
            print("Bum pulls out piece of paper with something written on it ")
            print("He quickly hands you the paper and disappears while you are carefully unfolding it ")
            print(f"'{clue}' is written on the paper")
            if clue not in code_collected:
                print(random.choice(code_dialogues1))
                code_collected.append(clue)
            elif code_collected == code:
                print("Seems like you finally have everything u needed to get to her..")
            else:
                print(random.choice(code_dialogues2))

        elif info_buy == 'no':
            print(f"{bum}: Stop bothering me then??")
            time.sleep(1)
            print(f"{bum} takes off and disappears to the crowds. ")
            return
        else:
            print("Invalid input, encounter will now end. Better luck next time. ")
            return


print_airport_comment = random.choice(airport_comment)



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

@app.route('/play_game', methods=['POST'])
def play_game():
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
    kaikki_funktiot()


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

@app.route('/make_bet', methods=['POST'])
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

    print("Your objective: \nFind Taylor Swifts lair and them "
          "\nvia purchasing information from various bums you encounter on your travels."
          "\nBeat Taylor Swift because she is very bad for the climate. ")






    while valinta not in (1, 2, 3):
        print("Invalid input ")
        valinta = int(input("Choose 1, 2, or 3 and press Enter to continue.."))
    else:
        selected_location = options[valinta - 1][0]
        kursori.execute("UPDATE game SET location = %s", (selected_location,))
        kursori.execute("SELECT location FROM game")
        sijainti = kursori.fetchone()
        print(f"U are at {sijainti[0]}")

    kursori.fetchall()

    while bum_count > 0:
        bum_encounter()
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
            break
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
            break

        print("Taylor's turn")
        time.sleep(1)
        print("You ready for your demice?")
        time.sleep(1)


        if chambers == bullet_chamber:
            print("BANG! Swift sucks!")
            time.sleep(1)
            break

        else:
            print("*Taylor pulls the trigger")
            time.sleep(1)
            print("Click! Taylor lives that one. :( ")
            chambers -= 1

def accept_boss_challenge():
    if code == code_collected:
        haaste = input("Are you ready to challenge Taylor 'The Final Boss' Swift ? \nInput yes / no\n")
        if haaste == "yes":
            money = "SELECT money FROM inventory WHERE amount = 2000"
            kursori.execute(money)
            tulos = kursori.fetchall()

            if tulos:
                boss_tasolle = input("U seem to be fit to start the final game, are you sure that you want to continue? \nInput yes / no\n")
                if boss_tasolle == "yes":
                    play_russian_roulette()
                elif boss_tasolle == "no":
                    print("Hahaha you are a bloody coward..")
                    travel()
            else:
                print("U need to have at least '25000' to play with her, you can't play with her")
                travel()

        if haaste == "no":
            print("What a coward..")
            travel()
            
def kaikki_funktiot():
    travel()
    bum_encounter()
"""