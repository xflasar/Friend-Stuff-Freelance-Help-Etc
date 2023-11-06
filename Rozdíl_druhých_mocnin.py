def decide(num1, num2):
    if num1 == num2:
        print("Numbers are equal.")
    else:
        larger_num = num1 if num1 > num2 else num2
        smaller_num = num2 if num1 > num2 else num1
        square_difference = abs(num1**2 - num2**2)

        if square_difference < 50:
            print(f"{larger_num} is greater than {smaller_num} and the difference of their squares is less than 50.")
        else:
            print(f"{larger_num} is greater than {smaller_num} and the difference of their squares is greater than or equal to 50.")

# Test cases:
decide(12, 13)
decide(14, 12)
decide(9, 9)
