import random

def guess_number_pc_pc(upper_bound):
    print(f"The computer will guess a number between 1 and {upper_bound}")

    target_number = random.randint(1, upper_bound)
    guess_count = 0

    lower_bound = 1
    current_guess = (lower_bound + upper_bound) // 2

    while current_guess != target_number:
        guess_count += 1

        if current_guess < target_number:
            lower_bound = current_guess + 1
        else:
            upper_bound = current_guess - 1

        current_guess = (lower_bound + upper_bound) // 2

    print(f"The computer guessed the number {target_number} in {guess_count} attempts.")

# Example usage:
guess_number_pc_pc(100)
