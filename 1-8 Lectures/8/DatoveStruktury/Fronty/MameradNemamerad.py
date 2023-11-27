def generate_bouquet():
    return [1, 2, 3, 4, 5]

def rearrange_bouquet(bouquet):
    original_bouquet = bouquet.copy()
    while True:
        first_petal = bouquet.pop(0)
        bouquet.append(first_petal)
        if bouquet == original_bouquet:
            break

def game():
    bouquet = generate_bouquet()
    rearrange_bouquet(bouquet)
    return bouquet

# Example usage:
result = game()
print(result)
