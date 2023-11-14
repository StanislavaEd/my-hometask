#Перевірити, чи є введене число парним.
print ("Введіть число")
num = int(input())

if num and not num % 2:
    print ( num, "парне число")
else:
    print ( num, " Не парне число")
