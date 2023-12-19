from random import *
from math import *

print("Добро пожаловать в программу проверки знаний по математике")

while True:
    try:
        dif = int(input("Выбери сложность(1-Easy/2-Medium/3-Hard): "))
        break
    except:
        print("Вы ввели неправильное значение")

print("Выбрана сложность {}".format(dif))

while True:
    try:
        q_quest = int(input("Введите количество вопросов: "))
        break
    except:
        print("Вы ввели неправильное значение")

print("Ответьте на {} вопроса(ов)".format(q_quest))
diff = [  [("+", "-")], [("+", "-", "/", "*")], [("+", "-", "/", "*", "**")]  ]

if dif >= 1 and dif <= 3:
    operations = diff[dif - 1]
else:
    print("Вы ввели неправильное значение уровня слоности")
    exit()
    
cor_answ = 0

if dif == 1:
    for x in range(q_quest):
        oper = choice(operations)
        print(oper)
        num1 = randint(-1,10)
        num2 = randint(-1,10)
        print(f"Решите пример: {num1} {oper} {num2}")
        answ = int(input("Введите свой ответ: "))
        
        if oper == "+":
            cor_answ = num1 + num2
            print("Правильно!") if cor_answ == answ else print("Неправильно")
            cor_answ += 1 if cor_answ == answ else None
            
        if oper == "-":
            cor_answ = num1 - num2
            print("Правильно!") if cor_answ == answ else print("Неправильно")
            cor_answ += 1 if cor_answ == answ else None
        