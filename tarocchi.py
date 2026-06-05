import random

# 1. The 22 Major Arcana with their French names
major_arcana = [
    "Le Mat", "Le Bateleur", "La Papesse", "L'Impératrice", "L'Empereur",
    "Le Pape", "L'Amoureux", "Le Chariot", "La Justice", "L'Ermite",
    "La Roue de Fortune", "La Force", "Le Pendu", "L'Arcane sans nom",
    "Tempérance", "Le Diable", "La Maison Dieu", "L'Étoile", "La Lune",
    "Le Soleil", "Le Jugement", "Le Monde"
]

print("Welcome, Chiccamandra. Shuffling the deck and drawing three cards for you... \n")

# 2. Draw 3 unique cards (no duplicates)
draw = random.sample(major_arcana, 3)

# 3. Define the three positions of the spread
positions = ["First card", "Second card", "Third card"]

# 4. Display the reading
for i in range(3):
    print(positions[i] + ": " + draw[i])

print("\nThe reading is complete. May the stars be in your favor!")