#Ввести число, вивести усі його дільники
print ("Введіть число")
y = int(input())
i = 1
while i <= y//2:
    if y % i == 0:
        print(i, end=' ')
    i+=1
print(y)
