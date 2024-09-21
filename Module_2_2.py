first = (input('Введите первое целое число'))
second = (input('Введите второе целое число'))
third = (input('Введите третье целое число'))
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)