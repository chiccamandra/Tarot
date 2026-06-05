# 1. Base sets in English (Knight moved to the end)
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Queen", "King", "Knight"]
suits = ["Wands", "Cups", "Pentacles", "Swords"]

# 2. Initialize the empty dictionary
minor_arcana_dict = {}

# 3. Counter for the dictionary keys (from 1 to 56)
card_id = 1

# 4. Cartesian product to generate the dictionary
for suit in suits:
    for value in values:
        card_name = value + " of " + suit
        
        # Assign the card to its numerical key
        minor_arcana_dict[card_id] = card_name
        
        # Increment the counter
        card_id = card_id + 1

# 5. Print the dictionary to verify the output
for key, name in minor_arcana_dict.items():
    print(key, ":", name)

print("\nTotal Minor Arcana generated:", len(minor_arcana_dict))