def largest(a, b, c):
    big = a
    if b > big:
        big = b
    if c > big:
        big = c
    return big

a = int(input())
b = int(input())
c = int(input())

print("Largest:", largest(a, b, c))
