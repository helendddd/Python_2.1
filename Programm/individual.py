#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi

if __name__ == '__main__':
    R = float(input("Enter outer radius... "))
    r = float(input("Enter inner radius... "))

    print("Ring ares is ", f"{pi * (R - r):.2f}")
