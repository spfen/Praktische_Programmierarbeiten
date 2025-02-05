# Stacks generieren - Der erste stäck ist voll die beiden anderen Stacks sind leer

hanoi_stack1 = [3, 2, 1] 
hanoi_stack2 = [] 
hanoi_stack3 = [] 
print("Wir spielen die Türme von Hanoi mit 3 Scheiben" + "\nDies ist die Ausgangslage")
print(hanoi_stack1, hanoi_stack2, hanoi_stack3)


hanoi_stack3.append(hanoi_stack1.pop())  # Von Stapel 1 nach Stapel 3 und Entfernung des Elementes im Stapel 1
print("\nUnd nun fangen wir an Züge zu nehmen:")
print(hanoi_stack1, hanoi_stack2, hanoi_stack3)

hanoi_stack2.append(hanoi_stack1.pop())  # Von Stapel 1 nach Stapel 2 und Entfernung des Elementes im Stapel 1
hanoi_stack2.append(hanoi_stack3.pop()) 
hanoi_stack3.append(hanoi_stack1.pop())
hanoi_stack1.append(hanoi_stack2.pop())
hanoi_stack3.append(hanoi_stack2.pop())
hanoi_stack3.append(hanoi_stack1.pop())
print("\nUnd damit sind wir fertig:")
print(hanoi_stack1, hanoi_stack2, hanoi_stack3)