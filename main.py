import numpy as np
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

def game_core_v3(number):
    count = 0
    predict = np.random.randint(1,100)
    x = abs(number - predict) #Вместо того, чтобы накручивать счётчик, прибавляем/убавляем разницу.
    while number != predict:
        count+=1
        if number > predict:
            predict += x
        elif number < predict:
            predict -= x
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(100))
    for number in random_array:
        count_ls.append(game_core(number))
    if int(np.mean(count_ls)) == 0:
        score = 1
    else:
        score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)