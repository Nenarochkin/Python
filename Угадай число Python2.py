﻿import random     #с помощью директивы import извлекаем функцию random- функция генератор случайных чисел

a=int(random.randint(1,10))#Переменной а присваеваем сгенерированное число и приводим его к целочисленному типу с помощью функции int()
b=''#Переменная которую будем использовать для ввода чисел Ей присваиваем значение пустую строку
print(a)# Выводим сгенерированное число для проверки
print('Угадай число\nВведите загаданное число')
while(b!=a):#Запускаем цикл и проверяем значение b, если b будет равна сгенерированному числу  выходим из цикла

     b=int(input())#Теперь с помощью функции input() вводим в консоль свой ответ, а с помощью функции int() делаем его целочисленным
     if(b==a):# Проверка ветвлением с помощью операторов if и elif проверяем введеннон значение
        print('Молодец!!!! Угадал')
     elif(b<a):#Если введенное число меньше загаданного выводим текст
             print(' Загаданное число  больше\n Введите еще раз ')
             b=int(input())#И вводим повторно
     elif(b>a):#Если введенное число больше загаданного выводим текст
             print('Загаданное число  меньше \nВведите еще раз ')
             b=int(input())#Вводим повторно


print('Молодец!!!! Угадал')