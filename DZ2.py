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
        count_eagle = 0
        count_tails = 0
       
        for i in range(len(many_list)):
            if many_list[i] == "0":
                count_eagle += 1
            elif many_list[i] == "1":
                count_tails += 1
            else:
                print(f"Ведено не верное значение:{many_list[i]} мы его не считаем")
        
        if count_eagle >= count_tails: invert = ('решки', count_tails)
        else: invert = ('орлы', count_eagle)
        
        print(f'Всего {count_tails + count_eagle} монет, из них орлов {count_eagle}, шт. и {count_tails}, шт.')
        print(f'Чтобы вcе монеты лежали одной стороной нужно: превернуть все "{invert}"')
      
    case 2:
        # Задача №2:
        # Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
        # а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
        # Пример:
        # 4 4 -> 2 2
        # 5 6 -> 2
        sum_n_m = int(input('Первая подсказка: Сумма двух чисел (N и M от 0 до 1000) ->  '))
        mult_n_m = int(input('Вторая подсказка: Произведение двух чисел (N и M от 0 до 1000) ->  '))
        for i in range(0, 1001):
            for j in range(0, 1001):
                if i+j == sum_n_m and i*j == mult_n_m: print (f'Загаданые числа {i} и {j}')
        else: print('таких чисел нет')
        
    case 3:

        # Задача №3:
        # Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
        # Пример:
        # 10 -> 1 2 4 8

        number = int(input('Введите до какого числа будем выводить степени 2:  '))
        i=0
        answer=[] 
        while 2**i < number:
            temp = 2**i 
            answer.append(temp)
            i+=1
        print(f'{number} -> {answer}')
            