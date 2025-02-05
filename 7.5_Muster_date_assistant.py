# Musterlösung MIT if & else!

# Musterlösung Kapiteltest 7.5
# TIP, Modul 2, HSLU
# 2023, Rachid Flückiger
import sys

# Kommandozeilenargumente speichern, noch nicht umgewandelt
day = sys.argv[1]
month = sys.argv[2]
year = sys.argv[3]

# 31er-Monate definieren
months_31 = [1, 3, 5, 7, 8, 10, 12]

print("\nWillkommen beim TIP-Datumsassistenten!")

# Kommandozeilenargumente nach Zulässigkeit prüfen
# Sind alle Kommandozeilenargumente Zahlen?
if day.isnumeric() and month.isnumeric() and year.isnumeric():
    day = int(day)
    year = int(year)
    month = int(month)
    # Sind die Zahlen im zulässigen Bereich?
    if (day > 0 and day < 32) and (month > 0 and month < 13) and (year > 0 and year < 10000):
        print("Dein Datum ist: " + str(day) + "." + str(month) + "." + str(year))
        # falls beides OK, starte nötige Berechnungen
        # Schaltjahrregeln anwenden
        if (year % 400 == 0):
            leap_year = True
        elif (year % 100 == 0):
            leap_year = False
        elif (year % 4 == 0):
            leap_year = True
        else:
            leap_year = False

        # Monatslänge bestimmen
        if month in months_31:
            month_length = 31
        elif month == 2:
            if leap_year:
                month_length = 29
            else:
                month_length = 28
        else:
            month_length = 30

        # Addition des Tages, plus Ausgabe
        if day < month_length:
            day = day + 1
        else:
            day = 1
            if month == 12:
                month = 1
                year = year + 1
            else:
                month = month + 1
        print("Der nächste Tag wird entsprechend " + str(day) +"."+ str(month) + "." + str(year) + " sein.\n")
    else:
        print("Eingabe nicht im zulässigen Bereich.\n")
else:
    print("Es wurden nicht nur Zahlen spezifiziert.\n")
