#!/usr/bin/env python

import unicornhat as uh
import time
import random
from colorsys import hsv_to_rgb

moves = [(0,1),(1,0),(0,-1),(-1.0),(-1,-1),(1,1),(1,-1),(-1,1)] #move up, down, left, right, or diagonal

uh.rotation(0)
uh.brightness(0.2)
x,y = uh.get_shape()


grid_size = (x,y)

x_mid = x // 2  # midpoint
y_mid = y // 2  # midpoint


x_pos = random.randint(0,range(x))
y_pos = random.randint(0,range(y))

grid_pos=(x_pos, y_pos)
dx, dy = random.choice(moves)

nsteps = 2000
hinc = 1/nsteps


for i in range(nsteps):
	un.set_pixel(x_pos,y_pos,75,100,100)
	un.show()
	
	while True:
		dx,dy = random.choice(moves)	
		x_pos + dx < x
		y_ops + dy < y
		if x_pos > x or y_pos > y
		
	time.sleep(.5)
