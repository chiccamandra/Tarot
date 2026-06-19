# ==========================================
# PART 1: GENERATE THE 8 BASE TRIGRAMS
# ==========================================

# 7 = Solid line (—)
# 8 = Broken line (- -)
possible_lines = [7, 8]
all_trigrams = []

# Generate all 8 combinations of 3 lines using nested loops
for line1 in possible_lines:
    for line2 in possible_lines:
        for line3 in possible_lines:
            trigram = [line1, line2, line3]
            all_trigrams.append(trigram)

# Verify the output by printing the list of trigrams
print("--- THE 8 GENERATED TRIGRAMS ---")
for i in range(len(all_trigrams)):
    print("Trigram", i + 1, ":", all_trigrams[i])

print("\nTotal trigrams in the set:", len(all_trigrams))

# ==========================================
# PART 2: GENERATE THE 64 HEXAGRAMS
# ==========================================

all_hexagrams = []

# Combine lower and upper trigrams (8 x 8 = 64 combinations)
for lower_trigram in all_trigrams:
    for upper_trigram in all_trigrams:
        
        # In Python, adding two lists '+' glues them together into a longer list of 6 items
        hexagram = lower_trigram + upper_trigram
        all_hexagrams.append(hexagram)

# Verify the output by printing the total number of hexagrams
print("--- HEXAGRAM SET INITIALIZED ---")
print("Total hexagrams generated in the database:", len(all_hexagrams))
