#!/usr/bin/env python3
#-*- coding:utf-8 -*-

fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 转换为摄氏度
    print("{:5d} {:10.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 25
