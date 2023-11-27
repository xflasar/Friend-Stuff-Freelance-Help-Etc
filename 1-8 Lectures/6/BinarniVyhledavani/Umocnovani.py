def super_power(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half_power = super_power(base, exp // 2)
        return half_power * half_power
    else:
        half_power = super_power(base, (exp - 1) // 2)
        return half_power * half_power * base

# Test the function
result = super_power(2, 5)
print(result)  # Output: 32
