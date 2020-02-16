import numpy as np
number = np.random.randint(1,100) 
print ("Загадано число от 1 до 99")

#Бинарный поиск

def game_core_v4(number):
    count = 0
    low = 1 # Нижняя граница поиска
    high = 99 # Верхняя граница поиска
    mid = 0 # Задаем переменную для середины, чтобы указать ее в условии цикла
    while number != mid and low < high: 
        count += 1
        mid = (low + high) // 2
        if number < mid: # Если загадонное число меньше середины, сдвигаем верхнюю границу к середине
            high = mid - 1 # Вычитаем 1, так как сама серидина уже сравнивалась и не подошла под условие
        elif number > mid: # Обратный случай, если загадонное число больше середины
            low = mid + 1
    return(count)

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v4) #В среднем выходит 5.434