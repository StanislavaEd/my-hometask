#Ви маєте три числа, вони вводяться з консолі.
#Перше число називається fizz, друге називається buzz.
#До третього необхідно дорахувати від одиниці.
#Дивлячись на поточне число, якщо воно
#кратне fizz – треба виводити F замість числа.
#Якщо число кратне buzz – треба виводити B замість числа.
#Якщо число кратне і fizz, і buzz, треба виводити FB.
#Якщо воно не кратне нічому, виводимо число.
#І так - поки не буде досягнуто третього введеного числа.
#Приклад умови та результату: Введено числа 2, 5, 18
#Висновок має бути таким:
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

print ("Введіть число fizz")
fizz = int(input())
print ("Введіть число buzz")
buzz = int(input())
print ("Введіть число total")
total = int(input())
result = []
for i in range(1,total+1):
    if not i % fizz and not i % buzz:
        result.append("FB")
    elif not i % fizz:
        result.append("F")
    elif not i % buzz:
        result.append("B")
    else:
        result.append(i)
print(result)

