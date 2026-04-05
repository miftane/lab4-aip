# 4.2.py
seat = int(input("Введите номер места (1-54): "))

if seat < 1 or seat > 54:
    print("Ошибка: неверный номер места")
elif seat <= 36:
    if seat % 2 == 0:
        print(f"Место {seat}: верхнее в купе")
    else:
        print(f"Место {seat}: нижнее в купе")
elif seat <= 54:
    if seat % 2 == 0:
        print(f"Место {seat}: верхнее боковое")
    else:
        print(f"Место {seat}: нижнее боковое")
