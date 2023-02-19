# Задача 34: 
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

text = ('пара-ра-рам рам-пам-папам па-ра-па-дам')
print(text)
text = text.split()


count = 0
glasnye = 'а'

for x in range(len(text)):
    for y in text[x]:
        if y == glasnye:
            count += 1
    if x == 0:
        a = count
        count = 0
    if x > 0:
        if a == count:
            count = 0
            if x == len(text) - 1:
                print('Парам пам-пам')
            continue
        if a != count:
            print("Пам парам")
            break