'''
Даны два целых числа А и В (A<B). Найти произведение всех целых чисел от А до В включительно.
'''

i = 0
while i == 0:
    try:
        A = int(input('Введите первое число: '))
        B = int(input('Введите второе число: '))
        AA = A
        S = 1
        if A < B:
            while A <= B:
                S *= A
                A += 1
            print(f'произведение чисел от {AA} до {B} равняется: {S}')
            i = 1
        else:
            print('Первое число должно быть меньше второго')
    except ValueError:
        print('Надо ввести число')
