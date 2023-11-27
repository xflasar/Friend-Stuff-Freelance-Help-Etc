def flatten_list(list_of_lists):
    # Vytvoříme nový seznam a přidáme do něj všechny prvky z jednotlivých seznamů
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    return flattened_list

# Příklad použití
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = flatten_list(nested_list)

print("Vstupní seznam seznamů:", nested_list)
print("Výsledek po zploštění:", result)
