def letterY(length, fill_char="#"):
    if length < 5:
        print("The size should be at least 5.")
        return

    for i in range(length):
        if i == 0:
            row = fill_char + "." * (length - 2) + fill_char
        elif i < length // 2:
            row = "." * (i) + fill_char + "." * (length - (i + i + 2)) + fill_char + "." * (i)
        else:
            if length % 2 == 0:
                row = "." * (length // 2 - 1) + fill_char * 2 + "." * (length // 2 - 1)
            else:
                row = "." * (length // 2) + fill_char + "." * (length // 2)
        print(row)

# Test cases:
letterY(5)
print()
letterY(8, "Y")
