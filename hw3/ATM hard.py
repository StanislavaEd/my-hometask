amount = int(input('Enter amount, pls'))
value = [10, 20, 50, 100, 200, 500, 1000]
result = {}
while amount % 10:
    amount = int(input('No, no, no. Enter your amount one more time '))
for one_value in value:
    num_of_value = min(amount // one_value, 10)
    if num_of_value:
        amount -= min(num_of_value * one_value, 10)
        print(f'{num_of_value} - {one_value}')
    if not amount:
        break
#ці задачки про банкомат доканали мене. Признаюсь чесно, для легкого банкомата пробувала той код,
# який пропонував Данііл, розбирала кожну строку і потім вже сама
# змогла написати за прикладом, але без заглядок в нього.
# А ось друга задача - фарт. Спробувала навмання і вийшло.
# Зато скільки щастя всередині відчула не передать словами
