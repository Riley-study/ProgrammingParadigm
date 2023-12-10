# Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

# Пример решения задачи с помощью бинарного поиска в функциональном стиле

def binary_search(array, target):
    """
    Рекурсивная функция для бинарного поиска элемента в отсортированном массиве.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    if not array:
        return -1
    middle_index = len(array) // 2
    middle_element = array[middle_index]
    if middle_element == target:
        return middle_index
    elif middle_element > target:
        return binary_search(array[:middle_index], target)
    else:
        result = binary_search(array[middle_index + 1:], target)
        return -1 if result == -1 else middle_index + 1 + result


# Пример использования функции
array = [1, 35, 51, 7, 9, 8, 100, 68, 4]
target = 9
result = binary_search(array, target)
print(result)
