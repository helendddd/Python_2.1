#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант №6
# С начала суток часовая стрелка повернулась на y градусов
# (0 <= y < 360, – вещественное число).
# Определить число полных часов и число полных минут, прошедших с начала суток.

import sys

if __name__ == '__main__':
    y = float(input("Enter degrees... "))

    if y < 0 or y > 360:
        print("Incorrect data entry!", file=sys.stderr)
    else:
        print("Hours passed: ", f"{y//15:.0f}")
        print("Minutes passed: ", f"{y//0.25:.0f}")
