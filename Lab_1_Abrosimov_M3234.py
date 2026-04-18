from math import cos, sin, asin
from time import time

lebesgueValue = 1 - cos(4) # Вычисляем через теорему об интеграле Римана и Лебега
lebesgueStieltjes = sin(1) + sin(2) + sin(3) + sin(4) # Вычислено в аналитической части

# Вычисление интеграла Лебега на промежутке, где sin >= 0
def getSinFirstPart(n):
    res = 0
    for k in range(n ** 2):
        res += k / n ** 2 * (asin((k + 1) / n ** 2) - asin(k / n ** 2))
    return 2 * res

# Вычисление интеграла Лебега на промежутке, где sin < 0
def getSinSecondPart(n):
    res = 0
    for k in range(n ** 2):
        if (k + 1) / n ** 2 < -sin(4):
            res += ((k + 1) / n ** 2) * (asin((k + 1) / n ** 2) - asin(k / n ** 2))
    return res

# Вычисление меры Лебега-Стилтьеса относительно точек, принадлежащих переданному множеству
def countMeasure(firstValue, secondValue, points):
    totalChanges = 0
    for point in points:
        if firstValue < abs(sin(point)) < secondValue:
            totalChanges += 1
    return totalChanges

# Вычисление интеграла Лебега-Стилтьеса на промежутке, где sin >= 0
def getStieltjesFirstPart(n):
    res = 0
    for k in range(n ** 2):
        res += k / n ** 2 * countMeasure(k / n ** 2, (k + 1) / n ** 2, [1, 2, 3])
    return res

# Вычисление интеграла Лебега-Стилтьеса на промежутке, где sin < 0
def getStieltjesSecondPart(n):
    res = 0
    for k in range(n ** 2):
        res += ((k + 1) / n ** 2) * countMeasure(k / n ** 2, (k + 1) / n ** 2, [4])
    return res

# Значения интеграла Лебега в при разных мелкостях разбиения
f_n = set()
# Итерации, на которых надо вывести статистику
nArray = [10, 100, 200, 300]
start = time()
for i in range(1, max(nArray) + 1):
    f_n.add(getSinFirstPart(i) - getSinSecondPart(i))
    if i in nArray:
        print("n = " + str(i) + " " + "значение интеграла Лебега = " + str(max(f_n)))
        print("Времени затрачено " + str(time() - start))
        print("Разница с аналитическим значением " + str(abs(lebesgueValue - max(f_n))))

# Значения интеграла Лебега-Стилтьеса в при разных мелкостях разбиения
f_n = set()
start = time()
for i in range(1, max(nArray) + 1):
    f_n.add(getStieltjesFirstPart(i) - getStieltjesSecondPart(i))
    if i in nArray:
        print("n = " + str(i) + " " + "значение интеграла Лебега-Стилтьеса = " + str(max(f_n)))
        print("Времени затрачено " + str(time() - start))
        print("Разница с аналитическим значением " + str(abs(lebesgueStieltjes - max(f_n))))
