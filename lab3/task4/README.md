# Задание №4 по варианту : `Точки и отрезки`

Студент ИТМО, Колпаков Артем Сергеевич 466237

## Вариант 12

## Задание 4

Допустим, вы организовываете онлайн-лотерею. Для участия нужно сделать
ставку на одно целое число. При этом у вас есть несколько интервалов после-
довательных целых чисел. В этом случае выигрыш участника пропорционален
количеству интервалов, содержащих номер участника, минус количество интер-
валов, которые его не содержат. (В нашем случае для начала - подсчет только
количества интервалов, содержащих номер участника). Вам нужен эффективный
алгоритм для расчета выигрышей для всех участников. Наивный способ сделать
это - просто просканировать для всех участников список всех интевалов. Однако
ваша лотерея очень популярна: у вас тысячи участников и тысячи интервалов. По
этой причине вы не можете позволить себе медленный наивный алгоритм

- Цель. Вам дается набор точек и набор отрезков. Цель состоит в том, чтобы
  вычислить для каждой точки количество отрезков, содержащих эту точку

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
   PYTHONPATH=. python3 lab3/task4/src/task.py
   ```

4. Запуск тестов:

   ```bash
   PYTHONPATH=. python3 lab3/task4/tests/test.py

   ```

## Тестирование

Для запуска тестов выполните:

```bash
    PYTHONPATH=. python3 lab3/task4/tests/test.py
```
