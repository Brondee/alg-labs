# Задание 8 по выбору : `Почти интерактивная хеш-таблица`

Студент ИТМО, Колпаков Артем Сергеевич 466237

## Вариант 12

## Задание 8

В данной задаче у Вас не будет проблем ни с вводом, ни с выводом. Просто
реализуйте быструю хеш-таблицу.
В этой хеш-таблице будут храниться целые числа из диапазона [0; 1015 − 1].
Требуется поддерживать добавление числа x и проверку того, есть ли в таблице
число x. Числа, с которыми будет работать таблица, генерируются следующим
образом. Пусть имеется четыре целых числа N, X, A, B такие что:

- 1 ≤ N ≤ 107
- 1 ≤ X ≤ 1015
- 1 ≤ A ≤ 103
- 1 ≤ B ≤ 1015
  Требуется N раз выполнить следующую последовательность операций:
- Если X содержится в таблице, то установить A ← (A + AC ) mod 103, B ←
  (B + BC ) mod 1015.
- Если X не содержится в таблице, то добавить X в таблицу и установить
  A ← (A + AD ) mod 103, B ← (B + BD ) mod 1015.
- Установить X ← (X · A + B) mod 1015.
  Начальные значения X, A и B, а также N, AC , BC , AD и BD даны во входном
  файле. Выведите значения X, A и B после окончания работы

## Input / Output

| Input   | Output |
| ------- | ------ |
| 4 0 0 0 | 3 1 1  |
| 1 1 0 0 |

## Ограничения по времени и памяти

- Ограничение по времени. 5сек.
- Ограничение по памяти. 256 мб.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Brondee/alg-labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd alg-labs
   ```
3. Запустите программу:

   ```bash
   PYTHONPATH=. python3 lab6/task8/src/task.py
   ```

4. Запуск тестов:

   ```bash
   PYTHONPATH=. python3 lab6/task8/tests/test_task_6_8.py

   ```

## Тестирование

Для запуска тестов выполните:

```bash
    PYTHONPATH=. python3 lab6/task8/tests/test_task_6_8.py
```
