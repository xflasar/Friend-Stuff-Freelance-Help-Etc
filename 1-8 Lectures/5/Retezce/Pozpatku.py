def reverse_string(input_string):
    # Použijeme řetězecový operátor [::-1] k obrácení řetězce
    reversed_string = input_string[::-1]
    return reversed_string

# Příklad použití
original_string = "Hello, World!"
result = reverse_string(original_string)

print("Původní řetězec:", original_string)
print("Obrácený řetězec:", result)
