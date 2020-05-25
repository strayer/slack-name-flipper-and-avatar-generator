import random

NAME = "Sven Grunewaldt"
# FLIPPED_NAME = "Sʌǝu ƃɹnuǝʍɐןpʇ"
FLIPPED_NAME = "Sʌǝn ƃɹunǝʍɐןpʇ"

# Find actually flipped characters for random choice
FLIPPED_CHARACTER_POSITIONS = [
    i for i in range(len(NAME) - 1) if NAME[i] != FLIPPED_NAME[i]
]


def flip_name():
    random_character_position = random.choice(FLIPPED_CHARACTER_POSITIONS)
    flipped_character = FLIPPED_NAME[random_character_position]

    name_with_flipped_character = list(NAME)
    name_with_flipped_character[random_character_position] = flipped_character

    return "".join(name_with_flipped_character)
