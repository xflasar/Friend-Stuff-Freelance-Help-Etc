def guess_number_pc(upper_bound):
    print(f"Think of a number between 1 and {upper_bound}")

    lower_bound = 1
    guess_count = 0

    while True:
        guess = (lower_bound + upper_bound) // 2
        guess_count += 1

        response = input(f"Is your number {guess}? (Enter 's' if it's smaller, 'b' if it's bigger, 'c' if it's correct): ")

        if response.lower() == 's':
            upper_bound = guess - 1
        elif response.lower() == 'b':
            lower_bound = guess + 1
        elif response.lower() == 'c':
            print(f"Yay! I guessed your number {guess} in {guess_count} attempts.")
            break
        else:
            print("Invalid input. Please enter 's', 'b', or 'c'.")

# Example usage:
guess_number_pc(100)
