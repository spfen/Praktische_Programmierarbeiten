# KAPITELTEST 7.5 - Date Assistant

import sys
from datetime import datetime, timedelta

# Überprüfen, ob das Datum über die Kommandozeile übergeben wurde
if len(sys.argv) != 2:
    print("Bitte ein Datum im Format dd.mm.jjjj angeben. Beispiel: python script.py 08.08.2024")
    sys.exit(1)  # System mit Fehlercode 1 beenden. Ein Wert ungleich Null wird als Fehlercode bewertet.

# Datum aus den Kommandozeilenargumenten einlesen
datum_input = sys.argv[1]

# Datum parsen
try:
    datum = datetime.strptime(datum_input, "%d.%m.%Y")
except ValueError:
    print(f"Das eingegebene Datum '{datum_input}' hat nicht das richtige Format. Bitte verwenden Sie dd.mm.jjjj.")
    sys.exit(1) # System mit Fehlercode 1 beenden. Ein Wert ungleich Null wird als Fehlercode bewertet.

print("Dein Datum ist: " + str(datum.strftime("%d.%m.%Y")))
# Einen Tag hinzufügen
neues_datum = datum + timedelta(days=1)

# Neues Datum im gleichen Format ausgeben
print("Der nächste Tag wird entsprechend " + neues_datum.strftime("%d.%m.%Y") + " sein.")
