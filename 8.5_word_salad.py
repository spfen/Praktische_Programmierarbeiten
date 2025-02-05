import random

# Eingabe der drei Sätze Subjekt-Verb-Adverb-Objekt

print("\nBitte gib mir 3 Sätze im Format: Subjekt - Verb - Adverb - Objekt")
sentence_1 = input("Gib mir den ERSTEN Satz: ")
sentence_2 = input("Gib mir den ZWEITEN Satz: ")
sentence_3 = input("Gib mir den DRITEN Satz: ")

# Listen erstellen
str_list_1 = sentence_1.split(" ")
str_list_2 = sentence_2.split(" ")
str_list_3 = sentence_3.split(" ")

# Die ursprüngliche Liste von Listen
originale_list = [str_list_1, str_list_2, str_list_3]

# Transponieren der Liste
transponierte_liste = list(zip(*originale_list))

# Zuweisung der transponierten Listen an separate Variablen
# part1 = list(transponierte_liste[0])
# part2 = list(transponierte_liste[1])
# part3 = list(transponierte_liste[2])
# part4 = list(transponierte_liste[3])

# Umwandlung der Tupel in Listen
transponierte_liste = [list(tupel) for tupel in transponierte_liste]

# Satz erstellen aus den zufällig generierten Elementen aus den Listen
sentence = []
for liste in transponierte_liste:
    r = random.randint(0, len(liste) - 1)
    sentence.append(liste[r])
print("\nDer Salat ist nun angerichtet:")
print(" ".join(sentence))