x = input("add or mult?: ")
def add_or_mult(a, b, x):
    if x == 'add':
        return a+b
    elif x == 'mult':
        return a*b
    else:
        print("Choose either add or mult")

print(add_or_mult(3, 5, x))