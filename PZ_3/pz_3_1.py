# вариант 28: Даны числа x, y. Проверить: точка лежит в I или III четверти.

while True:
    try:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        break
    except ValueError:
        print("Неправильно ввели!")

if (x > 0 and y > 0) or (x < 0 and y < 0):
    print("Истина")
else:
    print("Ложь")
