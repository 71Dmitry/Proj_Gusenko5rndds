'''
Даны три целых числа: А, В, С. Проверить истинность
 высказывания: «Число в находится между числами А и С».
'''


i = 0
while i == 0:
    print('Введите 3 числа:')
    A = float(input('Введите первое число: '))
    B = float(input('Введите второе число: '))
    C = float(input('Введите третье число: '))
    i = 1
    if A<B<C or A>B>C:
     print(f'Второе число со значением "{B}" находится посередине')
    else:
     print('числа расположены не по порядку')
