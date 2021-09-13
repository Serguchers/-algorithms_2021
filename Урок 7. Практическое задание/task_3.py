"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from statistics import median
from random import randint
from timeit import timeit

def find_median(Arr):
    stat_median = median(Arr)
    for i in range(len(Arr) // 2):
        Arr.remove(max(Arr))
    if stat_median == max(Arr):
        return max(Arr)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == '__main__':
    for i in range(100):
        size = randint(0, 100)
        TEST = [randint(-100, 100) for _ in range(2 * size + 1)]
        if not median(TEST) == find_median(TEST) == heap_sort(TEST)[size]:
            print('Ошибка')

    size = int(input('Введите размер массива:' ))
    TEST = [randint(-100, 100) for _ in range(2 * size + 1)]

    print(median(TEST[:]))
    print(timeit('median(TEST[:])', globals=globals(), number=1000))    # 0.008326000000000056
    print(find_median(TEST[:]))
    print(timeit('find_median(TEST[:])', globals=globals(), number=1000))   # 0.20960599999999996
    print(heap_sort(TEST[:])[size])
    print(timeit('heap_sort(TEST[:])[size]', globals=globals(), number=1000))    # 0.4140047

"""
m = 10
median - 0.0006209999999999827
find_median - 0.004766000000000048
heap_sort - 0.025450399999999984

m = 100
median - 0.005480699999999894
find_median - 0.20648179999999994
heap_sort - 0.4035204000000001

m = 1000
median - 0.1449145999999999
find_median - 20.301026900000004
heap_sort - 6.271150500000001

На рассмотренных размерах данных функция median модуля statistics была самой эффективной.
На маленьких данных функция find_median показывала лучший результат, чем поиск медианы при помощи сортировки кучей.
Однако по мере роста данных, количество перестановок, требуемое в find_median возрастает, следовательно, функция становится
медленней.
"""