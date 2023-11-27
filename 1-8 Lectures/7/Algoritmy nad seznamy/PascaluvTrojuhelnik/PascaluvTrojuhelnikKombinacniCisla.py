from math import comb

def pascal_binomial(n):
    triangle = [[comb(i, j) for j in range(i + 1)] for i in range(n)]
    return triangle

# Test the function
result = pascal_binomial(5)
print(result)
