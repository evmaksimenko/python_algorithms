# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
print("1. Случайное целое число")
print("2. Случайное вещественное число")
print("3. Случайный символ")
c = int(input("Введите номер варианта: "))
if c == 1:
    l = int(input("Нижняя граница: "))
    u = int(input("Верхняя граница: "))
    print("Случайное число %d" % random.randint(l, u))
elif c == 2:
    l = float(input("Нижняя граница: "))
    u = float(input("Верхняя граница: "))
    print("Случайное число %.3f" % random.uniform(l, u))
elif c == 3:
    l = input("Нижняя граница (один символ): ")
    u = input("Верхняя граница (один символ): ")
    print("Случайный символ %c" % chr(random.randint(ord(l), ord(u))))
else:
    print("Неверный выбор")