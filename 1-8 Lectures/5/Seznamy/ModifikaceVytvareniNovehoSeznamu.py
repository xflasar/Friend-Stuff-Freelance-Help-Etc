def double_all(input_list):
    # Vytvoříme nový seznam, kde každý prvek je dvojnásobkem odpovídajícího prvku vstupního seznamu
    doubled_list = [x * 2 for x in input_list]
    return doubled_list

def create_doubled(input_list):
    # Vytvoříme nový seznam, kde každý prvek je dvojnásobkem odpovídajícího prvku vstupního seznamu
    doubled_list = [x * 2 for x in input_list]
    return doubled_list

# Příklad použití
my_list = [1, 2, 3, 4, 5]
result_double_all = double_all(my_list)
result_create_doubled = create_doubled(my_list)

print("Vstupní seznam:", my_list)
print("double_all výsledek:", result_double_all)
print("create_doubled výsledek:", result_create_doubled)
