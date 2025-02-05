# KAPITELTEST 10.4 - Filter
import csv
from typing import List

my_list = [1,3,4,5,6,7,8,9,10]

# Funktion zum Filtern nach Geschlecht
def apply_gender_filter(data: List[str]) -> list:

    filtered_data = []
    gender_choice = input("Gib das Geschlecht ein. Female oder Male (f/m): ").strip().lower()

    # Überprüfen der Eingabe und Filtern nach Geschlecht
    if gender_choice not in ["f", "m"]:
        print("Ungültige Eingabe. Bitte 'f' für Female oder 'm' für Male eingeben.")
        return

    # Filtern und Speichern der gefilterten Ergebnisse
    for person in data[1:]:
        gender = person[4].strip().lower()  # Gender für jede Person separat extrahieren
        #if (gender_choice == "m" and gender == "male") or (gender_choice == "f" and gender == "female"):
        if gender_choice == gender[0]:
            filtered_data.append(person)
    return filtered_data


# Funktion zum Filtern nach Altersbereich
def apply_age_filter(data: list[str]) -> list:
    # Eingaben für den Filter
    try:
        min_year = int(input("Gib das tiefste Geburtsjahr ein (z.B. 1984): ").strip())
        max_year = int(input("Gib das höchste Geburtsjahr ein (z.B. 2017): ").strip())
    except ValueError:
        print("Bitte geben Sie gültige Zahlen für das Jahr ein.")
        return

    # Filtern und Speichern der gefilterten Ergebnisse nach Altersbereich
    for person in data:
        try:
            birth_year = int(person[7][:4])  # Extrahieren des Geburtsjahres
        except ValueError:
            continue  # Falls das Geburtsjahr nicht konvertierbar ist, diese Zeile überspringen

        if min_year <= birth_year <= max_year:
            filtered_data.append(person)


# Funktion zur Ausgabe der gefilterten Daten
def display_filtered_data():
    if len(filtered_data) > 1:  # Überprüfen, ob gefilterte Daten vorhanden sind
        for person in filtered_data[1:]:
            print(" | ".join(person))
    else:
        print("Keine Übereinstimmungen gefunden.")



# Definieren der Listen
data = []  # Daten von der CSV-Datei einlesen
filtered_data = []  # Enthält die gefilterten Daten

# Einlesen der CSV-Datei "people-100.csv"
with open("people-100.csv", "r") as input_file:
    reader = csv.reader(input_file)
    data = list(reader)  # Alle Zeilen in die data-Liste einlesen
    #if data:  # Überprüfen, ob die Datei nicht leer ist
    #    filtered_data.append(data[0])  # Hinzufügen der ersten Zeile (Header)


# Wähle den Filter
print("Wähle mit der dazugehörenden Zahl den Filter aus, den du verwenden möchtest:")
print("1: Geschlecht")
print("2: Altersbereich")
filter_number = input("Gib die Nummer des gewünschten Filters ein (1/2): ").strip()


# Funktion zum Wählen und Anwenden des Filters
def choose_filter():
    if filter_number == "1":
        subset_list = apply_gender_filter(data)
        subset_list = apply_age_filter(subset_list)
    elif filter_number == "2":
        apply_age_filter()
    else:
        print("Ungültige Auswahl. Bitte wähle 1 oder 2.")


# Anwenden des ausgewählten Filters
choose_filter()

# Ausgabe der gefilterten Daten
display_filtered_data()


# Funktion zur Wahl der Ausgabeart (Bildschirm oder Datei)
def choose_output():
    if len(filtered_data) > 1:
        print("\nSoll das Ergebnis auf dem Bildschirm oder in eine Datei ausgegeben werden?")
        print("'B' gibt auf den Bildschirm aus, 'D' speichert in eine Datei.")
        print("Enter ohne Eingabe ist standardmäßig Bildschirmausgabe.")
        output_mode = input("Ihre Wahl: ").strip().lower() or "b"  # Standardwert ist 'b' für Bildschirmausgabe

        if output_mode == "b":
            display_filtered_data()
        elif output_mode == "d":
            filename = input(
                "Bitte geben Sie einen Dateinamen ein (xxxx.csv, Enter verwendet Standardname): ").strip() or "persons.csv"
            with open(filename, "w",
                      newline='') as output_file:  # Nutzt newline='' um doppelten Zeilenabstand zu vermeiden
                writer = csv.writer(output_file)
                writer.writerows(filtered_data)
            print(f"Ergebnisse wurden in {filename} gespeichert.")
        else:
            print("Ungültige Auswahl. Ergebnisse werden standardmäßig auf dem Bildschirm ausgegeben.")
            display_filtered_data()
    else:
        print("Die Suche hat keine Ergebnisse geliefert.")


# Anwenden der Ausgabe
choose_output()