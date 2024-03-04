import random

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

user_input = input()
if user_input == "":
    print("Choose your starting point")

kursori.execute("SELECT airport.name, iso_country FROM airport ORDER BY RAND() LIMIT 3")
tulos = (kursori.fetchall())

for x in tulos:
    index = tulos.index(x)
    print(f"{index + 1}. {x}")

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
    #def blackJack(self):
        #deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
           #     "J","Q","K","A","J","Q","K","A","J","Q","K","A","J","Q","K","A",]

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
        Olio =Player
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