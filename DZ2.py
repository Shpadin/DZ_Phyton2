


task = int(input('введие номер задачи от 1 до 3: '))
match task:

    case 1:
 # Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
        many_list = list(input("введите (без пробелов) '0' если монета лежит орлом или '1' если монета лежит решкой:    "))
        print(f'Вы ввели следующие значения{many_list}')
        count_eagle=0
        count_tails=0
        for item in range(len(many_list)):
            if many_list[item] != '0' or '1': 
                print("Ведено не верное значение, повторите ввод")
        for i in range(len(many_list)):
            if many_list[i] == "0": 
                count_eagle += 1
            else: count_tails += 1
        print(f'Всего {count_tails+count_eagle} монет, из них орлов {count_eagle}, шт. и {count_tails}, шт.')
        print(f'Чтобы')
        # while number > 0:
        #     sum += number % 10
        #     number //= 10  
        # print(f'Сумма цифр в числе равна  {sum}')   
    case 2:
# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2
        numCranes = int(input('Введите количество журавликов:   '))
        number=numCranes
        sum =0
        while number > 0:
            sum += number % 10
            number //= 10  
        if sum%3 != 0:
             print(f"Такое количество {numCranes} целых Журавликов не могли сделать эти бракоделы")
        else:      
            print(f'Если всего было {numCranes} , то Катя из них сделала {(numCranes*2)/3} Журавликов, а Петя с Сережей сделали по {numCranes/6}')
            print(f'Петя, Катя и Сережа --> {int(numCranes/6)}, {int((numCranes*2)/3)}, {int(numCranes/6)}')
    case 3:

# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

        ticketnum = int(input('Введите 6 цфр билета:  '))
        number=ticketnum
        sum1=0
        sum2=0
        while number > 1000:
            sum1+=number%10
            number //= 10
            # print(number, sum1)
        print(f'ссума чисел правой части: {sum1}')
        
        while number > 0:
            sum2+=number%10
            number //= 10
            # print(number, sum2)
        print(f'ссума чисел левой части: {sum2}')
        
        if sum1 == sum2: 
            print('yes')
        else:
            print('no')
