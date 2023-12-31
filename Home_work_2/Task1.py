# На вход подается число n.
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

# Выбрана парадигма процедурного программирования для написания скрипта,
# так как задача заключается в выполнении набора последовательных действий.
def multiplication_table(n: int = 10) -> None:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i} * {j}  =  {i * j}')
    print()


if __name__ == '__main__':
    multiplication_table(5)
