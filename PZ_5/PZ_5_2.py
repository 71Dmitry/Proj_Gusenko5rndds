'''
Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
числу К справа цифру D (D - входной параметр целого типа, лежащий в диапазоне
0-9, K параметр целого типа, являющийся одновременно входным и выходным).
- С помощью этой функции последовательно добавить к данному числу К справа
данные цифры D1 и D2, выводя результат каждого добавления.
'''
def AddRightDigit(D, K):
    K = str(K) + str(D)
    return K


A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))

F = AddRightDigit(A, B)
print(F)
C = int(input('Введите второе число: '))
P = AddRightDigit(F,C)
print(P)
