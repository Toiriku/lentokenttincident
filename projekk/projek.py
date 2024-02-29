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

print("Tervetuloa Peliin!")
print("Press Enter to continue..")

user_input = input()
if user_input == "":
    print("Sinulla on 500 $, mihin haluaisit lähteä?")


kursori.execute ("SELECT airport.name FROM airport ORDER BY RAND() LIMIT 3")
tulos = (kursori.fetchall())

for x in tulos:
    index = tulos.index(x)
    print(f"{index + 1}. {x}")

start = input("Syötä joko 1,2 tai 3 ja paina Enter")

def startingPoint(start):
    print("Onnea matkaan!")
    valinta = tulos[int(start) - 1]
    kursori.execute("INSERT INTO game (location) VALUES (%s);", (valinta))
    print(f"Olet lentokentällä{valinta}")
    return

startingPoint(start)

print("Näet 3 henkilöä, kelle niistä haluat puhua?")
print("Henkilö 1, Henkilö 2, Henkilö 3")
print("Valitse numero ja paina Enter")