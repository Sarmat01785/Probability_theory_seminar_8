"""
Задача:
Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 131, 125, 115, 122, 131, 115, 107, 99, 125, 111. 
Известно, что в генеральной совокупности IQ распределен нормально. 
Найдите доверительный интервал для математического ожидания с надежностью 0.95.
"""

import numpy as np
from scipy import stats

# Значения IQ выборки студентов
iq_values = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

# Среднее значение выборки
mean_iq = np.mean(iq_values)

# Выборочное стандартное отклонение
std_iq = np.std(iq_values, ddof=1)

# Размер выборки
n = len(iq_values)

# Уровень доверия
confidence = 0.95
alpha = 1 - confidence

# Критическое значение t-распределения
t_critical = stats.t.ppf(1 - alpha / 2, df=n - 1)

# Вычисление доверительного интервала
margin_of_error = t_critical * (std_iq / np.sqrt(n))
confidence_interval = (mean_iq - margin_of_error, mean_iq + margin_of_error)

print(
    f"Доверительный интервал для математического ожидания IQ с надежностью 0.95: {confidence_interval}"
)
