import random
import timeit       # добавление библиотеки timeit
import matplotlib
import matplotlib.pyplot as plt
from random import choice


def _min(listy):
    mini = listy[1]
    for i in range(len(listy)):
        if listy[i] < mini:
            mini = listy[i]
    return mini



def _max(listy):
    maxy = listy[1]
    for i in range(len(listy)):
        if listy[i] > maxy:
            maxy = listy[i]
    return maxy


def _sum(listy):
    sumy = 0
    for i in range(len(listy)):
        sumy = sumy + listy[i]
    return sumy


def _mult(listy):
    multy = 1
    for i in range(len(listy)):
        multy = multy * listy[i]
    return multy

def generate_file(num):                           # заполнение файла случайными числами от 1 до num*50
    file = open("text.txt", 'w')
    for i in range(num*50):
        file.write(str(random.choice([i for i in range(-num*50, num*50) if i not in [0]]))+" ")
    file.close()


if __name__ == '__main__':

    num = int(input("введите кол-во тестов для посторения графика "))

    statistic_list = list()

    for i in range(0, num):
        generate_file(i+1)
        file = open('text.txt')
        mas = list(map(int, file.read().split()))  # считывание файла,перевод файла в список по численно,перевод чисел в float
        start_time = timeit.default_timer()         # запуск таймера (время начала)
        _sum(mas)
        finish_time = timeit.default_timer() - start_time
        statistic_list.append(finish_time)

    generate_file(1)                           # Т.е на 50 элементов от -50 до 50
    file = open('text.txt')
    mas = list(map(int, file.read().split()))

    #print(f"Сумма числе = {_sum(mas)}")
    #print(f"Произведение чисел = {_mult(mas)}")
    #print(f"Минимальное число = {_min(mas)}")
    #print(f"Максимальное число = {_max(mas)}")

    plt.plot(statistic_list)
    plt.show()

    #print(f"Время выполнения умножения = {timeit.default_timer() - start_time} с.")      # время конца - время начала