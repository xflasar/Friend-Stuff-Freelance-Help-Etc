def digit_sum(n):
    print(n % 10)
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(125))
print(digit_sum(58))
print(digit_sum(415458))