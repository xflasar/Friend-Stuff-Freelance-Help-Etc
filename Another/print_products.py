def print_products(n):
  for i in range(1,n+1):
    dem = n % i
    if dem == 0:
      print(str(n) + " = " + str(i) + " * " + str(round(n/i)))

print_products(36)