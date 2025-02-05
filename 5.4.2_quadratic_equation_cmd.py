import math, sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])



print("====================")
print("Deine Eingaben: \na = " + str(a) + ", " + "b = " + str(b) + ", " + "c = " + str(c))



# Diskriminate D definieren
D = round(b**2 - 4*a*c, 4)

# Verschiedene Lösungen definieren für D = 0, D > 0 und D > 0
if D < 0:
    print("Weil die Diskriminante D negativ ist, gibt es keine Lösung.")
elif D == 0:
    x = -b / ( 2 * a)
    print("Die Diskriminante D ist O und daher sind x1 und x2 gleich.")
    print(f"Lösung x = {x}")
else:
    sqrt_D = math.sqrt(D)
    x1 = (-b + sqrt_D) / (2 * a)
    x2 = (-b - sqrt_D) / (2 * a)
    print("\n\n====================" + "\nDaraus ergeben sich folgende Lösungen:")
    print("Diskriminante D = " + str(D))
    print("Lösung x_1 = " + str(x1) + "\nLösung x_2 = " + str(x2))

