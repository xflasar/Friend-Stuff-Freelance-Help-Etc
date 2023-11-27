def common_characters(str1, str2):
    # Získáme délku kratšího ze dvou řetězců
    length = min(len(str1), len(str2))

    # Projdeme každý znak na shodné pozici
    for i in range(length):
        if str1[i] == str2[i]:
            print(str1[i])

# Příklad použití
string1 = "hello"
string2 = "hola"

print("Shodné znaky na stejných pozicích:")
common_characters(string1, string2)
