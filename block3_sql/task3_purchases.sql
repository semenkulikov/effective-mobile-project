-- Блок 3: SQL
-- Задание 3: Покупки
--
-- Таблицы:
--   account (id, client_id, open_dt, close_dt)
--   transaction (id, account_id, transaction_date, amount, type)
--
-- Вывести ID клиентов, которые за последний месяц по всем своим счетам
-- совершили покупок меньше, чем на 5000 рублей.
-- Без использования подзапросов и оконных функций.

-- Решение: Используем JOIN и GROUP BY с HAVING

-- Шаг 1: Определяем последний месяц (предполагаем, что это текущий месяц или последние 30 дней)
-- Шаг 2: Соединяем account и transaction по account_id
-- Шаг 3: Фильтруем транзакции за последний месяц и только покупки (type = 'BUY' или аналогичный)
-- Шаг 4: Группируем по client_id
-- Шаг 5: Суммируем amount и фильтруем по условию < 5000

-- Вариант 1: Если "последний месяц" означает текущий месяц
SELECT 
    a.client_id
FROM account a
INNER JOIN transaction t ON a.account_id = t.account_id
WHERE 
    -- Транзакции за текущий месяц
    DATE_TRUNC('month', t.transaction_date) = DATE_TRUNC('month', CURRENT_DATE)
    -- Только покупки (предполагаем, что type содержит 'BUY' или это положительные суммы)
    -- Нужно уточнить формат type, но обычно покупки имеют type = 'BUY' или 'PUR'
    AND t.type IN ('BUY', 'PUR', 'PURCHASE')  -- уточнить формат type
    -- Счет должен быть открыт на момент транзакции
    AND (a.close_dt IS NULL OR t.transaction_date <= a.close_dt)
    AND t.transaction_date >= a.open_dt
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;

-- Вариант 2: Если "последний месяц" означает последние 30 дней
SELECT 
    a.client_id
FROM account a
INNER JOIN transaction t ON a.account_id = t.account_id
WHERE 
    -- Транзакции за последние 30 дней
    t.transaction_date >= CURRENT_DATE - INTERVAL '30 days'
    AND t.transaction_date < CURRENT_DATE
    -- Только покупки
    AND t.type IN ('BUY', 'PUR', 'PURCHASE')  -- уточнить формат type
    -- Счет должен быть открыт на момент транзакции
    AND (a.close_dt IS NULL OR t.transaction_date <= a.close_dt)
    AND t.transaction_date >= a.open_dt
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;

-- Вариант 3: Более универсальный (если type может быть любым, но покупки - это положительные amount)
-- Или если покупки определяются по типу транзакции (нужно уточнить бизнес-логику)
SELECT 
    a.client_id
FROM account a
INNER JOIN transaction t ON a.account_id = t.account_id
WHERE 
    -- Транзакции за последний календарный месяц
    t.transaction_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
    AND t.transaction_date < DATE_TRUNC('month', CURRENT_DATE)
    -- Только покупки (предполагаем, что это транзакции с определенным типом)
    -- Если type = 'DEB' или отрицательные значения - это покупки, нужно уточнить
    AND t.type = 'DEB'  -- уточнить формат type для покупок
    -- Счет должен быть открыт на момент транзакции
    AND (a.close_dt IS NULL OR t.transaction_date <= a.close_dt)
    AND t.transaction_date >= a.open_dt
GROUP BY a.client_id
HAVING SUM(ABS(t.amount)) < 5000;

-- Примечания:
-- 1. Нужно уточнить формат поля type для определения покупок
-- 2. Нужно уточнить определение "последний месяц" (календарный месяц или последние 30 дней)
-- 3. Учитываем, что счет должен быть открыт на момент транзакции
-- 4. Используем только JOIN и GROUP BY без подзапросов и оконных функций
