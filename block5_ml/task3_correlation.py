"""
Блок 5: ML Base
Задание 3: Ручной счёт корреляции

Рассчитайте линейную корреляцию Пирсона на основе данных.
Какой вывод можно сделать на основе полученного результата?
Можно ли утверждать, что существует причинно-следственная связь между количеством чашек кофе,
выпитых студентами в течение экзаменационного дня, и их итоговым баллом за экзамен?

Ответ округлить до сотых, например: 4,12

Число выпитых чашек кофе | Балл за экзамен
1                        | 85
1                        | 88
2                        | 79
2                        | 81
2                        | 84
2                        | 65
3                        | 67
3                        | 58
3                        | 76
4                        | 49
"""

import numpy as np
import math


def pearson_correlation(x, y):
    """
    Вычисляет коэффициент корреляции Пирсона.
    
    Формула: r = Σ((xi - x̄)(yi - ȳ)) / √(Σ(xi - x̄)² * Σ(yi - ȳ)²)
    """
    n = len(x)
    
    # Вычисляем средние значения
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    # Вычисляем числитель: Σ((xi - x̄)(yi - ȳ))
    numerator = np.sum((x - mean_x) * (y - mean_y))
    
    # Вычисляем знаменатель: √(Σ(xi - x̄)² * Σ(yi - ȳ)²)
    sum_sq_diff_x = np.sum((x - mean_x) ** 2)
    sum_sq_diff_y = np.sum((y - mean_y) ** 2)
    denominator = math.sqrt(sum_sq_diff_x * sum_sq_diff_y)
    
    if denominator == 0:
        return 0.0
    
    correlation = numerator / denominator
    return correlation


# Данные из задания
coffee = np.array([1, 1, 2, 2, 2, 2, 3, 3, 3, 4])
score = np.array([85, 88, 79, 81, 84, 65, 67, 58, 76, 49])

print("=" * 80)
print("РАСЧЕТ КОРРЕЛЯЦИИ ПИРСОНА")
print("=" * 80)

print("\nДанные:")
print("Чашки кофе | Балл")
print("-" * 25)
for i in range(len(coffee)):
    print(f"{coffee[i]:10d} | {score[i]:4d}")

# Вычисляем корреляцию
correlation = pearson_correlation(coffee, score)

print("\n" + "=" * 80)
print("ХОД РЕШЕНИЯ:")
print("=" * 80)

print("\n1. Вычисляем средние значения:")
mean_coffee = np.mean(coffee)
mean_score = np.mean(score)
print(f"   Среднее количество чашек кофе: {mean_coffee:.2f}")
print(f"   Средний балл: {mean_score:.2f}")

print("\n2. Вычисляем отклонения от среднего:")
print("   Чашки | Балл | (xi - x̄) | (yi - ȳ) | (xi - x̄)(yi - ȳ)")
print("   " + "-" * 60)
for i in range(len(coffee)):
    diff_x = coffee[i] - mean_coffee
    diff_y = score[i] - mean_score
    product = diff_x * diff_y
    print(f"   {coffee[i]:6d} | {score[i]:4d} | {diff_x:8.2f} | {diff_y:8.2f} | {product:13.2f}")

print("\n3. Вычисляем корреляцию Пирсона:")
numerator = np.sum((coffee - mean_coffee) * (score - mean_score))
sum_sq_diff_coffee = np.sum((coffee - mean_coffee) ** 2)
sum_sq_diff_score = np.sum((score - mean_score) ** 2)
denominator = math.sqrt(sum_sq_diff_coffee * sum_sq_diff_score)

print(f"   Числитель: Σ((xi - x̄)(yi - ȳ)) = {numerator:.2f}")
print(f"   Σ(xi - x̄)² = {sum_sq_diff_coffee:.2f}")
print(f"   Σ(yi - ȳ)² = {sum_sq_diff_score:.2f}")
print(f"   Знаменатель: √(Σ(xi - x̄)² * Σ(yi - ȳ)²) = {denominator:.2f}")
print(f"   r = {numerator:.2f} / {denominator:.2f} = {correlation:.2f}")

print("\n" + "=" * 80)
print(f"КОЭФФИЦИЕНТ КОРРЕЛЯЦИИ ПИРСОНА: {correlation:.2f}")
print("=" * 80)

print("\nИНТЕРПРЕТАЦИЯ:")
print(f"Коэффициент корреляции r = {correlation:.2f}")

if abs(correlation) < 0.3:
    strength = "слабая"
elif abs(correlation) < 0.7:
    strength = "умеренная"
else:
    strength = "сильная"

if correlation < 0:
    direction = "отрицательная"
    print(f"Наблюдается {strength} {direction} корреляция.")
    print("Чем больше чашек кофе, тем ниже балл за экзамен.")
else:
    direction = "положительная"
    print(f"Наблюдается {strength} {direction} корреляция.")
    print("Чем больше чашек кофе, тем выше балл за экзамен.")

print("\n" + "=" * 80)
print("ВЫВОДЫ О ПРИЧИННО-СЛЕДСТВЕННОЙ СВЯЗИ:")
print("=" * 80)

print("\n❌ НЕТ, нельзя утверждать о причинно-следственной связи на основе корреляции.")
print("\nПричины:")
print("1. Корреляция не означает причинность (correlation ≠ causation)")
print("2. Возможны скрытые переменные:")
print("   - Стресс (высокий стресс → больше кофе + ниже балл)")
print("   - Недостаток сна (недосып → больше кофе + ниже балл)")
print("   - Уровень подготовки (низкая подготовка → больше кофе + ниже балл)")
print("3. Возможна обратная причинность:")
print("   - Низкий балл может вызывать стресс, который приводит к большему потреблению кофе")
print("4. Небольшой размер выборки (n=10) не позволяет делать надежные выводы")
print("5. Могут быть выбросы и другие факторы, влияющие на результат")

print("\nДля установления причинно-следственной связи необходимо:")
print("- Провести контролируемый эксперимент")
print("- Учесть все возможные смешивающие переменные")
print("- Использовать больший размер выборки")
print("- Применить методы причинного вывода (causal inference)")
