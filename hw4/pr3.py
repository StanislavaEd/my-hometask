#проверить каждую строку файла, если строка записана верно, вывести ее и после написать True,
# если строка не верна, вывести результат с пометкой False.
with open('pr3_list.txt', 'r') as f:
    for line in f.readlines():
        plus, how = line.strip().split(";")
        elems = [int(s) for s in plus.strip().split(" ")]
        div, rem = how.strip().split(" ")
        result = sum(elems) % len(elems) == int(rem) and sum(elems) // len(elems) == int(div)
        print(f"{line} {result}",)
    else:
        print(f"{line}", "False")


