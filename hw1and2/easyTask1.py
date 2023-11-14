#Надрукувати "We are the champions" за допомогою коду.
s = '1.We ARE the Champions'
print (s)
#Надрукувати "We are the champions", поклавши 'champions'
# у окрему змінну. Використати конкатенацію (склійку рядків через плюс).
d = '2.We'
w = 'Champions'
print (d + ' ARE the ' + w)
#Виконати передоднє завдання, користуючись форматуваннями через відсоток.
e = '3.We are the'
r = 'Champions'
print('%s  %s' % (e,r))
#Виконати передоднє завдання, користуючись форматуваннями через метод format.
t1 = "4.We {} {} champions!"
print(t1.format("are","the"))
#Виконати передоднє завдання, користуючись форматуваннями через префікс f.
who = "We"
message = (
    f'5.{who} are the champions'
)
print(message)
#Ввести імʼя, надрукувати "Hello, " й додати імʼя, яке було введено.
# Склійку робити за допомогою префіксу f.
name = "Stasya"
say = (f'6.Hello {name}')
print(say)
#Ввести два імені, надрукувати рядок, де буде написано, що перше імʼя
#та друге імʼя пішли гуляти. Наприклад, якщо введені Alex та Mary,
#надрукувати "Alex and Mary go for a walk.", за допомогою префіксу.
name1 = "Victor"
name2 = "Vasya"
evening = (f'7.{name1} and {name2} go for a walk')
print(evening)

#вести два цілих числа, трансформувати їх до цілих чисел, скласти, надрукувати суму.
int1 = 5
int2 = 7
y = int1+int2
print(int(y))
#Ввести три цілих числа, трансформувати до цілих чисел, надрукувати суму.
a = input('Input number')
b = input('Input number')
result = a + b
text = "Result" + str(result)
print(text)
#Ввести два цілих числа num1, num2 й один рядок str1, надрукувати
# "num1 and num2 are str1", використовувати форматування f.
a = input("number_1")
b = input("number_2")
c = input("str1")
text = (f'a,b,c')
print(text)
