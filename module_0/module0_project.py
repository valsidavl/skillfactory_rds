import random
import numpy as np


def predict_algorithm():
    '''Функция угадывает число. Устанавливается случаное число в пределах от 1 до 100, 
затем загаданное число сравнивается с серединой последовательности(в нашем случае 50)
и в зависимости от того, больше оно или меньше правая или левая граница ряда чисел 
становится в два раза меньше, после чего этот процесс происходит пока загаданное и
угадываемое числа не совпадут. Возращается число попыток, счет начинается с момента 
первого выбора середины последовательности
    '''
    target = random.randint(1, 100)
    predict = 50
    count = 1
    right_border = 101
    left_border = 0
    while target != predict:

        if target < predict:
            right_border = predict
            predict = (right_border + left_border)//2
            count += 1

        elif target > predict:
            left_border = predict
            predict = (right_border + left_border)//2
            count += 1

    return count


def score_attempt():
    '''Функция подсчета среднего количества попыток алгоритма угадывания числа'''
    test_mean_list = []
    for iterator in range(1000):
        test_mean_list.append(predict_algorithm())
    
    mean_count = round(np.mean(test_mean_list), 0)
    
    return mean_count

print("Алгоритм угадывает число в среднем за {} попыток".format(score_attempt()))
