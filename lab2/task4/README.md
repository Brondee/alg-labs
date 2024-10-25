# 4 задача. Бинарный поиск

В этой задаче вы реализуете алгоритм бинарного поиска, который позволяет
очень эффективно искать (даже в огромных) списках при условии, что список
отсортирован. Цель - реализация алгоритма двоичного (бинарного) поиска.

- Формат входного файла (input.txt). В первой строке входного файла со-
  держится число n (1 ≤ n ≤ 105) — число элементов в массиве, и последо-
  вательность a0 < a1 < ... < an−1 из n различных положительных целых
  чисел в порядке возрастания, 1 ≤ ai ≤ 109 для всех 0 ≤ i < n. Следующая
  строка содержит число k, 1 ≤ k ≤ 105 и k положительных целых чисел
  b0, ...bk−1, 1 ≤ bj ≤ 109 для всех 0 ≤ j < k.
- Формат выходного файла (output.txt). Для всех i от 0 до k − 1 вывести
  индекс 0 ≤ j ≤ n − 1, такой что ai = bj или -1, если такого числа в массиве
  нет.
- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.

## Запуск тестов

- `PYTHONPATH=. python3 task4/tests/test.py `