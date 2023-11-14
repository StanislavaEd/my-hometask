#Створити словник оцінок передбачуваних студентів
# (Ключ – ПІ студента, значення – список оцінок студентів).
# Знайти найуспішнішого і самого слабенького за середнім балом.
voc = {"bob": [5, 4, 3, 4], "bill": [2, 3, 3, 5], "jack": [5, 4, 5]}
new_voc = {"best": ("", 1),"worst": ("", 6) }
for name, marks in voc.items():
    avg = round(sum(marks)/len(marks),3)
    if avg >= float( new_voc.get("best")[1]):
        new_voc['best'] = (name, avg)
    if avg <= float (new_voc.get("worst")[1]):
        new_voc['worst'] = (name, avg)
print (f"best of the best is {new_voc.get('best')}")
print (f"worst of the worst is {new_voc.get('worst')}")
