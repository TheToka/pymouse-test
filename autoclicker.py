# -*- coding: utf-8 -*-

import time
from time import sleep
from pymouse import PyMouse

print ("Сколько кликов? ")

kol = input()

m = PyMouse()
i = 0
#test t

while i < kol:
	m.click(1100, 490, 1)#1 - lbm. 2 - rbm
	sleep(0.01)
	i += 1
	print(str(i) + "/" + str(kol))
