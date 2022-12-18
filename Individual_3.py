#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = input("Введите предложение")
b = input("Введите нижнюю границу")
c = input("Введите верхнюю границу")

x = int(b)
y = int(c)+1

r = a[:x] + a [y:]

print (r)