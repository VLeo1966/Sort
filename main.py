import time

# Декоратор для замера времени выполнения функции
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Записываем время начала
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Записываем время окончания
        elapsed_time = end_time - start_time  # Вычисляем время выполнения
        print(f"Время выполнения {func.__name__}: {elapsed_time:.5f} секунд")
        return result
    return wrapper

# Пример использования декоратора
@measure_time
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Вызываем функцию для замера времени
example_function(1000000)
