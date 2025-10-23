# 1. Demander les notes
notes = []
n = int(input("Combien de matières ? "))

for i in range(n):
    note = float(input(f"Note {i+1} : "))
    notes.append(note)

# 2. Calculer la moyenne
moyenne = sum(notes) / len(notes)

# 3. Afficher le résultat
print(f"La moyenne est : {moyenne:.2f}")

