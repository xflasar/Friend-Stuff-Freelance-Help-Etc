def fibonacci(n):
    fib_sequence = [1, 1]  # První dva prvky Fibonacciho posloupnosti

    for _ in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence[:n]

# Příklad použití pro vypsání prvních 10 prvků Fibonacciho posloupnosti
n = 10
fibonacci_sequence = fibonacci(n)
print(f"Prvních {n} prvků Fibonacciho posloupnosti: {fibonacci_sequence}")
