# 4.4.py
color1 = input("Введите первый цвет (красный, синий, желтый): ").lower()
color2 = input("Введите второй цвет: ").lower()

colors = {"красный", "синий", "желтый"}

if color1 not in colors or color2 not in colors:
    print("Ошибка: можно использовать только красный, синий или желтый")
else:
    if {color1, color2} == {"красный", "синий"}:
        print("Фиолетовый")
    elif {color1, color2} == {"красный", "желтый"}:
        print("Оранжевый")
    elif {color1, color2} == {"синий", "желтый"}:
        print("Зеленый")
    else:
        print("Цвет не изменится (смешали одинаковые)")
