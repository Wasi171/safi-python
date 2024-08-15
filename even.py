num = int(input('enter number'))
cal = num % 2
if cal == 0:
    print(f'{num} is even')
elif cal != 0:
    print(f'{num} is odd')