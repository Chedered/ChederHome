import numpy as np
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

def game_core_v3(number):
    count = 0
    predict = np.random.randint(1,100)
    dif = abs(number - predict) #Вместо того, чтобы накручивать счётчик, прибавляем/убавляем разницу.
    #Так как счетчик не крутиться, если числа изначально равны, 
    #а алгоритм всегда угадывает с первого раза,
    #крутим счетчик при равенстве.
    #Так количество попыток не будет падать ниже единицы на дистанции.
    if number == predict:
        count+=1
    else:
        while number != predict:
            count+=1
            if number > predict:
                predict += dif
            elif number < predict:
                predict -= dif
    return(count) # выход из цикла, если угадали

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

score_game(game_core_v3)