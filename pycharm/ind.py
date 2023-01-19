#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


array = []
result = None
size = int(input('Введите размер последовательности: '))

for i in range(1, size + 1):
    array.append(random.randrange(1, 10000))
print(array)

for i in range(len(array)):
    if (array[i]) > (array[i + 1]):
        result = array[i + 1]
        break

if result is None:
    print('Последовательность упорядочена')
else:
    print('Первое число, нарушающее упорядоченность: ', result)
