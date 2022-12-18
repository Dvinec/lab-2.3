#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
   text = input("Введите текст: ")

   sentence = text.split('.')
r = sentence.pop(0)
x = r.count('и')

if x== 0:
   print("В первом предложении нет буквы И")

else:
   print (x)