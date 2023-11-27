def tetranacci(n, memo={}):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    elif n in memo:
        return memo[n]
    else:
        result = tetranacci(n-1, memo) + tetranacci(n-2, memo) + tetranacci(n-3, memo) + tetranacci(n-4, memo)
        memo[n] = result
        return result

# Test the function
n = 10
result = tetranacci(n)
print(f"The {n}-th Tetranacci number is: {result}")
