# name = input('Введите ваше имя: ')
# if name == 'Mariya' :
#     print('Здравствуйте, администратор')
# else:
#     print('Привет, ', name)
number = int(input('Введите число:')) #Fizz, Buzz, FizzBuzz
if number % 3 == 0 or number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число не подходит')


