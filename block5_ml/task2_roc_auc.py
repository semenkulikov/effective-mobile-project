"""
Блок 5: ML Base
Задание 2: Ручной счёт ROC_AUC

Классификатор выдал следующие прогнозируемые метки класса и вероятности принадлежности к классу "1".
На основе полученных данных рассчитайте метрику ROC_AUC. Тезисно описать ход решения.

Ответ округлить до сотых, например: 4,12

Истинная метка класса | Порог классификации (0.6) | Оценка вероятности
1                     | 1                          | 0.95
0                     | 1                          | 0.9
1                     | 1                          | 0.85
0                     | 1                          | 0.8
1                     | 1                          | 0.75
1                     | 1                          | 0.7
1                     | 1                          | 0.65
1                     | 1                          | 0.6
0                     | 0                          | 0.55
0                     | 0                          | 0.5
0                     | 0                          | 0.45
1                     | 0                          | 0.4
0                     | 0                          | 0.35
0                     | 0                          | 0.3
0                     | 0                          | 0.25
"""

import numpy as np


def calculate_roc_auc(y_true, y_scores):
    """
    Вычисляет ROC-AUC вручную.
    
    Алгоритм:
    1. Сортируем данные по убыванию вероятностей
    2. Для каждого порога вычисляем TPR и FPR
    3. Строим ROC-кривую
    4. Вычисляем площадь под кривой (AUC) методом трапеций
    """
    # Сортируем по убыванию вероятностей
    sorted_indices = np.argsort(y_scores)[::-1]
    y_true_sorted = y_true[sorted_indices]
    y_scores_sorted = y_scores[sorted_indices]
    
    # Подсчитываем количество положительных и отрицательных примеров
    n_pos = np.sum(y_true == 1)
    n_neg = np.sum(y_true == 0)
    
    if n_pos == 0 or n_neg == 0:
        return 0.5
    
    # Инициализируем переменные
    tpr = [0.0]  # True Positive Rate
    fpr = [0.0]  # False Positive Rate
    tp = 0
    fp = 0
    
    # Вычисляем TPR и FPR для каждого порога
    for i in range(len(y_true_sorted)):
        if y_true_sorted[i] == 1:
            tp += 1
        else:
            fp += 1
        
        tpr.append(tp / n_pos)
        fpr.append(fp / n_neg)
    
    # Вычисляем AUC методом трапеций
    auc = 0.0
    for i in range(1, len(fpr)):
        auc += (fpr[i] - fpr[i-1]) * (tpr[i] + tpr[i-1]) / 2.0
    
    return auc


# Данные из задания
y_true = np.array([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0])
y_scores = np.array([0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25])

print("=" * 80)
print("РУЧНОЙ РАСЧЕТ ROC-AUC")
print("=" * 80)

print("\nХОД РЕШЕНИЯ:")
print("1. Сортируем данные по убыванию вероятностей")
print("2. Для каждого порога вычисляем:")
print("   - TPR (True Positive Rate) = TP / (TP + FN)")
print("   - FPR (False Positive Rate) = FP / (FP + TN)")
print("3. Строим ROC-кривую (FPR по оси X, TPR по оси Y)")
print("4. Вычисляем площадь под кривой (AUC) методом трапеций\n")

# Подсчитываем количество классов
n_pos = np.sum(y_true == 1)
n_neg = np.sum(y_true == 0)

print(f"Количество положительных примеров (класс 1): {n_pos}")
print(f"Количество отрицательных примеров (класс 0): {n_neg}\n")

# Сортируем по убыванию вероятностей
sorted_indices = np.argsort(y_scores)[::-1]
y_true_sorted = y_true[sorted_indices]
y_scores_sorted = y_scores[sorted_indices]

print("Отсортированные данные (по убыванию вероятности):")
print("Вероятность | Истинный класс")
print("-" * 40)
for i in range(len(y_scores_sorted)):
    print(f"{y_scores_sorted[i]:.2f}        | {y_true_sorted[i]}")

# Вычисляем ROC-AUC
auc = calculate_roc_auc(y_true, y_scores)

print("\n" + "=" * 80)
print(f"ROC-AUC = {auc:.2f}")
print("=" * 80)

# Детальный расчет для понимания
print("\nДетальный расчет:")
print("Порог | TP | FP | TN | FN | TPR    | FPR")
print("-" * 60)

tp = 0
fp = 0
tn = n_neg
fn = n_pos

for i in range(len(y_true_sorted)):
    threshold = y_scores_sorted[i]
    if y_true_sorted[i] == 1:
        tp += 1
        fn -= 1
    else:
        fp += 1
        tn -= 1
    
    tpr_val = tp / n_pos if n_pos > 0 else 0
    fpr_val = fp / n_neg if n_neg > 0 else 0
    
    print(f"{threshold:.2f} | {tp:2d} | {fp:2d} | {tn:2d} | {fn:2d} | {tpr_val:.3f} | {fpr_val:.3f}")

print(f"\nИтоговый ROC-AUC: {auc:.2f}")
