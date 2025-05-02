def f(pos_only_1,/,pos_or_kwd,*,kwd_only_1):
    print(pos_only_1,pos_or_kwd,kwd_only_1)
f(1,pos_or_kwd = 2,kwd_only_1 = "Hej")

#   HELP

def f(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        raise ValueError('Choose either "add" or "multiply"')


print(f(2, 5, 'add'))
print(f(2, 5, 'multiply'))

try:
    print(f(2, 5, 'test'))
except ValueError as e:
    print(e)