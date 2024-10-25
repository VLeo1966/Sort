import time


# Декоратор для замера времени выполнения функции сортировки
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Время выполнения {func.__name__}: {elapsed_time:.5e} секунд")
        return result

    return wrapper


# Пузырьковая сортировка
@measure_time
def bubble_sort(arr, iterations):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            iterations[0] += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# Сортировка вставками
@measure_time
def insert_sort(arr, iterations):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            iterations[0] += 1
        arr[j + 1] = key
        iterations[0] += 1  # Считаем итерацию для случая, когда условие не выполняется
    return arr


# Сортировка выбором
@measure_time
def selection_sort(arr, iterations):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            iterations[0] += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Итеративная быстрая сортировка
@measure_time
def quick_sort_iterative(arr, iterations):
    # Стек для подмассивов
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()  # Получаем границы подмассива

        if low < high:
            pivot_index = partition(arr, low, high, iterations)

            # Добавляем подмассивы в стек
            stack.append((low, pivot_index - 1))  # Левая часть
            stack.append((pivot_index + 1, high))  # Правая часть

    return arr


# Вспомогательная функция для разделения подмассива
def partition(arr, low, high, iterations):
    pivot = arr[high]  # Опорный элемент - последний элемент подмассива
    i = low - 1  # Индекс для большего элемента

    for j in range(low, high):
        iterations[0] += 1  # Увеличиваем счетчик итераций
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Перемещаем опорный элемент на его правильное место
    return i + 1


# Функция для замера времени и выполнения сортировки
def measure_sort_time_and_iterations(sort_func, arr):
    iterations = [0]  # Счетчик итераций
    sorted_arr = sort_func(arr[:], iterations)  # Копируем массив, чтобы не модифицировать оригинал
    return sorted_arr, iterations[0]


# Массив из 10 случайных чисел
array = [10, -3, 7, 2, -5, 6, 0, -8, 9, 1]

# Выполняем сортировку для каждого метода и выводим результаты
for sort_name, sort_func in [
    ('Bubble Sort', bubble_sort),
    ('Insertion Sort', insert_sort),
    ('Selection Sort', selection_sort),
    ('Quick Sort (Iterative)', quick_sort_iterative)
]:
    sorted_array, iteration_count = measure_sort_time_and_iterations(sort_func, array)
    print(f"{sort_name}:")
    print(f"Sorted Array: {sorted_array}")
    print(f"Iterations: {iteration_count}\n")
