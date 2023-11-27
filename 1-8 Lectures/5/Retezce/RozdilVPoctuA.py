def compare_a_counts(str1, str2):
    # Spočítáme počet 'a'/'A' v prvním řetězci
    count_str1 = str1.lower().count('a')

    # Spočítáme počet 'a'/'A' v druhém řetězci
    count_str2 = str2.lower().count('a')

    # Porovnáme počty a vypíšeme informaci
    if count_str1 < count_str2:
        print(f"Řetězec 1 obsahuje méně 'a'/'A' než řetězec 2. Rozdíl: {count_str2 - count_str1}")
    elif count_str1 > count_str2:
        print(f"Řetězec 2 obsahuje méně 'a'/'A' než řetězec 1. Rozdíl: {count_str1 - count_str2}")
    else:
        print("Počet 'a'/'A' v obou řetězcích je stejný.")

# Příklad použití
string1 = "apple"
string2 = "Banana"

compare_a_counts(string1, string2)
