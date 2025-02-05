import random
import csv

# Gewinn-Tabelle einlesen
gewinn_tabelle = {}
with open('gewinn_tabelle.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        gewinn_tabelle[tuple(row[:-1])] = int(row[-1])

# Eingabe der Anzahl Nickels
nickels = int(input("Gib die Anzahl der Nickels an, die du einsetzen möchtest: "))
list_rad = ["Huf", "Karo", "Herz", "Pik", "Glocke"]

while nickels > 0:
    # Generieren und Anzeigen der Kombination
    combination = [random.choice(list_rad) for _ in range(3)]
    print(f"Dein Einsatz: {nickels}, Kombination: {combination}")
    
    # Gewinnüberprüfung mit der Tabelle
    gewinn = gewinn_tabelle.get(tuple(combination), 0)
    if gewinn > 0:
        nickels += gewinn
        print(f"SUUUUPER! Du hast {gewinn} Nickels gewonnen! Neuer Stand: {nickels}")
    else:
        nickels -= 1
    
    # Überprüfung, ob Nickels übrig sind
    if nickels == 0:
        print("Keine Nickels mehr übrig, das Spiel ist vorbei.")
        break
    
    # Frage, ob weiterspielen
    if input("Möchtest du weitermachen? (j/n): ").lower() == "n":
        print("Das Spiel wurde beendet.")
        break

print("Vielen Dank fürs Spielen!")


# KAPITELTEST 9.5 - Liberty Bell

import random
import csv

# Gewinn-Tabelle einlesen
auszahlungen = {}
with open('gewinn_tabelle.csv', mode='r') as file:
    reader = csv.reader(file,delimiter=';')
    for row in reader:
        combination = tuple(row[:-1])
        payout = int(row[-1])
        auszahlungen[combination] = payout

print(combination)
print(payout)
print(auszahlungen)


# Eingabe der Anzahl Nickels
spieler_nickels = int(input("Gib die Anzahl der Nickels an, die du einsetzen möchtest: "))
maschine_nickels = 20

list_rad = ["Huf", "Karo", "Herz", "Pik", "Glocke"]

while spieler_nickels > 0 and maschine_nickels > 0:
    # Generieren und Anzeigen der Kombination
    combination = tuple(random.choice(list_rad) for _ in range(3))
    print(f"\nDein Einsatz: {spieler_nickels}, Kombination: {combination}")
    
    # Gewinnüberprüfung und Auszahlung
    gewinn = auszahlungen.get(combination, 0)
    if gewinn > 0:
        if gewinn <= maschine_nickels:
            spieler_nickels += gewinn
            maschine_nickels -= gewinn
            print(f"SUUUUPER! Du hast {gewinn} Nickels gewonnen! Dein aktueller Stand: {spieler_nickels}, Nickels in der Maschine: {maschine_nickels}")
        else:
            print(f"Die Maschine hat nicht genug Nickels für diese Auszahlung. Verbleibende Nickels in der Maschine: {maschine_nickels}")
    else:
        print("Keine Auszahlung für diese Kombination.")
        
    
    # Einsatz reduzieren und Spiel beenden, wenn keine Nickels übrig sind
    spieler_nickels -= 1
    if spieler_nickels == 0:
        print("Keine Nickels mehr übrig, das Spiel ist vorbei.")
        break
    
    # Frage, ob weiterspielen
    if input("Möchtest du weitermachen? (j/n): ").lower() == "n":
        print("Das Spiel wurde beendet.")
        break
    
     # Spiel beenden, wenn die Maschine keine Nickels mehr hat
    if maschine_nickels == 0:
        print("Die Maschine hat keine Nickels mehr. Das Spiel ist vorbei.")
        break

print("Vielen Dank fürs Spielen!")






### Ursprünglich 

import random

# Eingabe der Anzahl Nickels
nickels = int(input("Gib die Anzahl der Nickels an, die du einsetzen möchtest: "))
list_rad = ["Huf", "Karo", "Herz", "Pik", "Glocke"]

while nickels > 0:
    # Generieren und Anzeigen der Kombination
    combination = [random.choice(list_rad) for _ in range(3)]
    print(f"Dein Einsatz: {nickels}, Kombination: {combination}")
    
    # Gewinnüberprüfung
    if combination.count(combination[0]) == 3:
        print("SUUUUPER! Du hast gewonnen!")
        break
    
    # Einsatz reduzieren und Spiel beenden wenn keine Nickels übrig sind
    nickels -= 1
    if nickels == 0:
        print("Keine Nickels mehr übrig, das Spiel ist vorbei.")
        break
    
    # Frage, ob weiterspielen
    if input("Möchtest du weitermachen? (j/n): ").lower() == "n":
        print("Das Spiel wurde beendet.")
        break

print("Vielen Dank fürs Spielen!")
