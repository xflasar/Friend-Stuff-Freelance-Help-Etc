def censor_string(input_string):
    # Převedeme řetězec na list, abychom mohli snadno modifikovat jednotlivé znaky
    characters = list(input_string)

    # Projdeme každý druhý znak a nahradíme ho za X
    for i in range(1, len(characters), 2):
        characters[i] = 'X'

    # Sestavíme modifikovaný řetězec z listu znaků
    censored_string = ''.join(characters)
    return censored_string

# Příklad použití
original_text = "This is a sample text for censorship."
censored_text = censor_string(original_text)

print("Původní text:", original_text)
print("Cenzurovaný text:", censored_text)
