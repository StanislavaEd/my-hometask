#Банкомат видає суму максимально можливими купюрами
amount = int(input('Enter amount, pls'))
value = [1000, 500, 200, 100, 50, 20, 10]
result = []
while amount % 10:
    amount = int(input('No, no, no. Enter your amount one more time '))
for one_value in value:
    num_of_value = amount // one_value
    if num_of_value:
        amount -= num_of_value * one_value
        print(f'{num_of_value} - {one_value}')
    if not amount:
        break
