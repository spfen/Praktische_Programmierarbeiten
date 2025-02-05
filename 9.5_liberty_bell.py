# KAPITELTEST 9.5 - Liberty Bell

import random
import csv

# Gewinn-Tabelle einlesen als Dictionary
  # Dieser Code liest eine CSV-Datei, bei der jede Zeile aus einer Kombination von Werten und einem dazugehörigen Auszahlungsbetrag besteht.
  # Die Kombination wird als Schlüssel in einem Dictionary gespeichert, und der Auszahlungsbetrag wird als der entsprechende Wert gespeichert.
  # Am Ende enthält das Dictionary auszahlungen alle Kombinationen und ihre zugehörigen Auszahlungsbeträge aus der CSV-Datei.
auszahlungen = {}
with open("gewinn_tabelle.csv", "r") as file:
    reader = csv.reader(file,delimiter=";")
    for line in reader:
        combination = tuple(line[:-1])
        payout = int(line[-1])
        auszahlungen[combination] = payout

# Eingabe der Anzahl Nickels
while True:
    spieler_nickels = int(input("Gib die Anzahl der Nickels an, die du einsetzen möchtest: "))
    if spieler_nickels > 0:
        break
    else:
        print("Bitte gib eine positive Zahl ein. DANKE!")  

maschine_nickels = 20
list_rad = ["Huf", "Karo", "Herz", "Pik", "Glocke"]

# Gewinnrad laufen lassen
while spieler_nickels > 0 and maschine_nickels > 0:
    # Generieren und anzeigen der Kombination
    # Wählt dreimal ein zufälliges Element aus der Liste list_rad aus.
    # Die drei Elemente werden
    # in einem Tuple gespeichert und der Variablen combination zugewiesen.
    combination = tuple(random.choice(list_rad) for _ in range(3))
    print(f"\nDein Einsatz: {spieler_nickels}, Kombination: {combination}")
    
    # Gewinnüberprüfung und Auszahlung
      # Der Code prüft, ob eine bestimmte Kombination zu einer Auszahlung führt.
    gewinn = auszahlungen.get(combination, 0) # Wenn die combination im Dictionary auszahlungen nicht vorhanden ist, wird 0 zurückgegeben.
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