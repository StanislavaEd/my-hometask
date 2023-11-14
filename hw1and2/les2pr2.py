#Перевірити, чи є число не парним, ділиться чи на три
#і на п'ять одночасно, але так, щоб не ділитися на 10.
print ("Введіть число")
y = int(input())

if y and y % 2 and not y % 3 and not y % 5 and y % 10:
    print("You are cool", y)
else :
    print("Try again later" )
