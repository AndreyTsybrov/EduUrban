print('Задача «Длина слова»')
a=('hello')
print(len(a))

print('Задача «Суммы и разности»')
first=(5)
second=(7)
summa=(first + second)
diff=(first - second)
print('summa =',(summa)), print('diff =',(diff))

print('Задача «Среднее арифметическое»')
import statistics
first=(6)
second=(4)
third=(9)
numbers=[first, second, third]
mean=statistics.mean(numbers)
print(mean)

print('Задача «Простые строчки»')
first_string=('Вторник')
second_string=('Понедельник')
print(str(second_string)+',', first_string)

print('Задача «Сложная формула»')
a=(2)
b=(4)
c=(7)
f=((a * b) + (a * c))
result=(f**3/2)
print(result)