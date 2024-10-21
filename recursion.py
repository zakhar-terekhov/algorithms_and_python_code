def print_numbers(n: int, a=1):
    """Печатает числа от 1 до n."""
    if a <= n:
        print(a)
        print_numbers(n, a + 1)


def multiplie_two_numbers(x, y):
    """Возвращает произведение двух чисел."""
    if x == 0:
        return x
    return y + multiplie_two_numbers(x - 1, y)


def return_sum_number_array(array, index=0):
    """Возвращает сумму всех чисел списка."""
    if index == len(array):
        return 0
    return array[index] + return_sum_number_array(array, index + 1)


def return_max_number_array(array, index=0):
    """Возвращает максимальное число из списка."""
    if index == len(array):
        return array[0]
    return max(array[index], return_max_number_array(array, index + 1))


def raise_to_power(a, x):
    """
    Возводит число в степень

    :param a: Основание степени
    :param x: Показатель степени
    """
    if x == 0 or x == 1:
        return a
    return a * raise_to_power(a, x - 1)


def return_sum_numbers(n):
    if n == 0:
        return 0
    return n + return_sum_numbers(n - 1)
