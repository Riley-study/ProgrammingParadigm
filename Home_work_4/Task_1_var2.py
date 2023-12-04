import numpy as np

# два массива случайных величин
x = np.array([1, 2, 3, 4, 5])
y = np.array([-1, -2, -3, -4, -5])

# расчет коэффициента корреляции Пирсона
corr_coef = np.corrcoef(x, y)[0, 1]

print("Коэффициент корреляции Пирсона:", round(corr_coef))
