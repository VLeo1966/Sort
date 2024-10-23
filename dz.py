import time

# Функция для замера времени и выполнения сортировки
def measure_sort_time_and_iterations(sort_func, arr):
    iterations = [0]  # Используем список для передачи по ссылке
    start_time = time.perf_counter()  # Используем более точный таймер
    sorted_arr = sort_func(arr[:], iterations)  # Копируем массив, чтобы не модифицировать оригинал
    end_time = time.perf_counter()
    sort_time = end_time - start_time
    return sorted_arr, sort_time, iterations[0]

# Пузырьковая сортировка
def bubble_sort(arr, iterations):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            iterations[0] += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Сортировка вставками
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
def selection_sort(arr, iterations):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            iterations[0] += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Быстрая сортировка
def quick_sort(arr, iterations):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    iterations[0] += len(arr) - 1  # Количество сравнений в текущем вызове
    return quick_sort(left, iterations) + [pivot] + quick_sort(right, iterations)

# Массив из 10 случайных чисел
array = [10, -3, 7, 2, -5, 6, 0, -8, 9, 1]

# Выполняем сортировку для каждого метода и выводим результаты
for sort_name, sort_func in [
    ('Bubble Sort', bubble_sort),
    ('Insertion Sort', insert_sort),
    ('Selection Sort', selection_sort),
    ('Quick Sort', quick_sort)
]:
    sorted_array, time_taken, iteration_count = measure_sort_time_and_iterations(sort_func, array)
    print(f"{sort_name}:")
    print(f"Sorted Array: {sorted_array}")
    print(f"Time taken: {time_taken:.2e} seconds")  # Форматируем время в научной нотации
    print(f"Iterations: {iteration_count}\n")
