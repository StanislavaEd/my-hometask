#Вам известен номер квартиры, этажность дома и количество квартир на этаже.
# Задача: написать функцию, которая по заданным параметрам напишет вам,
# в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.
import math
flat = int(input("Введіть номер квартири"))
floor = int(input("Введіть кількість поверхів"))
apartments = int(input("Введіть кількість квартир на поверсі"))
entrance = int(input("Введіть кількість підїздів"))
building = floor*apartments*entrance
result = 0
while flat > building:
     flat= int(input('Забагато для такого будинку, введіть номер квартири ще раз'))
i = (flat - 1) // (floor *apartments) + 1
y = ((flat - 1) % (floor * apartments) // apartments +1)
print(f' підїзд, {i}, поверх, {y}')

