def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(is_triangle(3, 4, 5))
print(is_triangle(3, -4, 5))
print(is_triangle(7, 2, 6))
print(is_triangle(3, 12, 5))
print(is_triangle(7, 2, 5))
print(is_triangle(4, 4, 4))