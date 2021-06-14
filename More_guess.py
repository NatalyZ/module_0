import numpy as np

def game_core_v2(number):
    '''Задаем левую и правую границу числового отрезка, выбинраем середину, сравниваем с загаданным число.
    Если загаданное больше середины, смещаем левую границу в текущую середину + 1.
    Если загаднное меньше середины, смещаем правую границу в текущую середину.
    Поиск будет закончен, когда числовой отрезок сойдется в одном загаданном числе.
    Реализация бинарного поиска.'''
    count = 0
    left = 1
    right = 100
    predict = np.random.randint(1, 101)   # загадать число
    while left < right:
        number = (right + left)//2     # рассчитать середину
        if predict > number:
            left = number + 1      # сдвинуть левую границу в середину + 1
        else:
            right = number   # сдвинуть правую границу в середину
        count += 1
    return count     # выход из цикла, если угадал

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

score_game(game_core_v2)