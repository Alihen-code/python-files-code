def create_character(name, strength, intelligence, charisma):
    # --- name validation ---
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    # --- stats validation ---
    stats = (strength, intelligence, charisma)

    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'
    if any(s < 1 for s in stats):
        return 'All stats should be no less than 1'
    if any(s > 4 for s in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'

    def bar(value):
        return '●' * value + '○' * (10 - value)

    return (
        f'{name}\n'
        f'STR {bar(strength)}\n'
        f'INT {bar(intelligence)}\n'
        f'CHA {bar(charisma)}'
    )


# --- gather input in the program, not the function ---
name = input('Enter your character name: ')
print(create_character(name, 4, 2, 1))