# Лабораторная работа №7: `Динамическое программирование №1`

Студент ИТМО, Колпаков Артем Сергеевич 466237

## Вариант 12

### Навигация

- [ ] [Задача 1 - Обмен монет](task1/)
- [ ] [Задача 2 - Примитивный калькулятор](task2/)
- [ ] [Задача 4 - Наибольшая общая подпоследовательность двух последовательностей](task4/)
- [ ] [Задача 5 - Наибольшая общая подпоследовательность трех последовательностей](task5/)

## Описание

В данной лабораторной работе изучается мощный инструмент, динамическое
программирование.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Brondee/alg-labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd alg-labs
   ```
3. **Запуску всех задач**

   ```bash
   for script in lab7/*/src/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done

   ```

4. **Запуску всех тестов задач**

   ```bash
   for script in lab7/*/tests/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done

   ```

## Тестирование

Для запуска тестов выполните:

```bash
python3 -m pytest -v lab7/task*/tests/*.py

```