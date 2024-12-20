# Задание №1 по варианту : `Улучшение Quick sort`

Студент ИТМО, Колпаков Артем Сергеевич 466237

## Вариант 12

## Задание 1

Основное задание. Цель задачи - переделать данную реализацию рандо-
мизированного алгоритма быстрой сортировки, чтобы она работала быстро
даже с последовательностями, содержащими много одинаковых элементов.
Чтобы заставить алгоритм быстрой сортировки эффективно обрабатывать
последовательности с несколькими уникальными элементами, нужно заме-
нить двухстороннее разделение на трехстороннее (смотри в Лекции 3 слайд
17).

## Input / Output

| Input | Output |
| ----- | ------ |
| 4     | 1      |
| + 1   | 10     |
| + 10  |
| -     |
| -     |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
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
   PYTHONPATH=. python3 lab3/task1/src/task.py
   ```

4. Запуск тестов:

   ```bash
   PYTHONPATH=. python3 lab3/task1/tests/test.py

   ```

## Тестирование

Для запуска тестов выполните:

```bash
    PYTHONPATH=. python3 lab3/task1/tests/test.py
```
