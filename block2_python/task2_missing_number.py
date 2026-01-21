"""
Блок 2: Python
Задание 2: Натуральная последовательность

Реализовать функцию (или тело функции), которая находит единственное отсутствующее число
из последовательности натуральных чисел 1,2,…,n.

Пример:
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))
# Вывод: 
7

Оценить оптимальность решения по времени и памяти и прикрепить текст кода.
"""


def missing_number(nums):
    """
    Находит единственное отсутствующее число в последовательности натуральных чисел 1..n.
    
    Алгоритм:
    Сумма арифметической прогрессии от 1 до n: S = n * (n + 1) / 2
    Если в массиве отсутствует одно число, то:
    - Находим сумму всех чисел в массиве
    - Вычисляем ожидаемую сумму для последовательности 1..n
    - Разница даст нам отсутствующее число
    
    Временная сложность: O(n), где n - длина массива
    Пространственная сложность: O(1) - используем только константное количество переменных
    """
    if not nums:
        return None
    
    # Находим максимальное число в массиве (это n)
    n = max(nums)
    
    # Вычисляем ожидаемую сумму последовательности 1..n
    expected_sum = n * (n + 1) // 2
    
    # Вычисляем фактическую сумму чисел в массиве
    actual_sum = sum(nums)
    
    # Разница даст нам отсутствующее число
    missing = expected_sum - actual_sum
    
    return missing


def missing_number_alternative(nums):
    """
    Альтернативное решение через XOR.
    
    Идея: используем свойство XOR: a ^ a = 0 и a ^ 0 = a
    Если выполнить XOR всех чисел от 1 до n и всех чисел в массиве,
    то отсутствующее число останется.
    
    Временная сложность: O(n)
    Пространственная сложность: O(1)
    """
    if not nums:
        return None
    
    n = max(nums)
    
    # XOR всех чисел от 1 до n
    xor_expected = 0
    for i in range(1, n + 1):
        xor_expected ^= i
    
    # XOR всех чисел в массиве
    xor_actual = 0
    for num in nums:
        xor_actual ^= num
    
    # Результат - отсутствующее число
    return xor_expected ^ xor_actual


if __name__ == "__main__":
    # Тестовые примеры
    nums1 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
    result1 = missing_number(nums1)
    print(f"missing_number({nums1}) = {result1}")  # 7
    
    nums2 = [1, 2, 3, 5]
    result2 = missing_number(nums2)
    print(f"missing_number({nums2}) = {result2}")  # 4
    
    nums3 = [2, 3, 4, 5]
    result3 = missing_number(nums3)
    print(f"missing_number({nums3}) = {result3}")  # 1
    
    # Проверка альтернативного решения
    print(f"\nАльтернативное решение (XOR):")
    print(f"missing_number_alternative({nums1}) = {missing_number_alternative(nums1)}")
