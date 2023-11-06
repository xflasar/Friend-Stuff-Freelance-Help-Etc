def powers(base, n):
    return [base**i for i in range(n+1)][1:]
    
print(powers(2, 7))