# A list of animals
animals = ["Lion", "Elephant", "Dolphin", "Eagle", "Panda", "Whale"]

# Looping through the list of animals
for animal in animals:
    if animal == "Dolphin":
        break  # 'break' will exit the loop when it encounters "Dolphin"
    print(animal)  # Prints the current animal before encountering "Dolphin"


# Modified version: using 'continue' instead of 'break'
for animal in animals:
    if animal == "Dolphin":
        continue  # 'continue' will skip the rest of the loop when it encounters "Dolphin", but continue looping
    print(animal)  # Prints the current animal, except for "Dolphin"


# Looping through numbers from 0 to 10
for i in range(11):
    if i % 2 != 0:  # Checks if the number is odd
        continue  # 'continue' skips the rest of the loop for odd numbers
    print(i)  # Prints the number if it's even (i.e., when i % 2 == 0)
