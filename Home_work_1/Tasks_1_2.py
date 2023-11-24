# Задача 1.
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для сортировки чисел в списке
# в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers: list) -> list:
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


numbers = [1, 250, 812, 52, 11, 1]

print("Отсортированный список (императивно):", sort_list_imperative(numbers))


# Задача 2.
# Написать точно такую же процедуру, но в декларативном стиле.

def sort_list_declarative(numbers: list) -> list:
    numbers.sort()
    return numbers


numbers2 = [1000, 10, 25, 12, 512, 101]

print("Отсортированный список (декларативно):", sort_list_declarative(numbers2))
