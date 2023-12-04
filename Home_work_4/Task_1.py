# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно
# упростит вам жизнь
import math


def pearson_corr(x, y) -> float:
    # вычисление средних значений
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    #     вычисление средних отклонений
    x_dev = [xi - x_mean for xi in x]
    y_dev = [yi - y_mean for yi in y]

    #  вычисление ковареации
    cov = sum([x_dev[i] * y_dev[i] for i in range(len(x))])/len(x)

    #     вычисление стандартных отклонений

    x_std = math.sqrt(sum([(xi - x_mean) ** 2 for xi in x]) / len(x))
    y_std = math.sqrt(sum([(yi - y_mean) ** 2 for yi in y]) / len(y))

    #     вычисление коэффициента корреляции
    corr_cof = cov / (x_std * y_std)
    return corr_cof


first_list = [1, 2, 3, 4, 5]
second_list = [-1, -2, -3, -4, -5]

corr_cof = pearson_corr(first_list, second_list)
print("Коэффициент корреляции Пирсона: ", round(corr_cof))
