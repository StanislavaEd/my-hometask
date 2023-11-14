#Написати fizzbuzz для 20 комплектів по три числа,
# які записані в файл. Читайте із файлу перший рядок
# з трьома числами, беріть із нього числа, рахуйте для
# них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
file_list = 'list.txt'
with open(file_list) as f:
    for line in f:
        f, b, n = map(int, line.split())
        result = []

        for i in range(1, n+1):
            if not i % f and not i % b:
                result.append("FB")
            elif not i % f:
                result.append("F")
            elif not i % b:
             result.append("B")
            else:
                result.append(str(i))
        print(" ".join(result))
