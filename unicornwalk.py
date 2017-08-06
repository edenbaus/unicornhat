#!/usr/bin/env python

import unicornhat as uh
import time
import random
from colorsys import hsv_to_rgb

moves = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)] #move up, down, left, right, or diagonal
print ('set moves')

uh.set_layout(uh.AUTO)
#uh.rotation(0)
uh.brightness(0.3)
x,y = uh.get_shape()
#y,x = len(uh.PHAT), len(uh.PHAT[0])

def set_boarder(r,g,b):
#	boarder = [(xi,yi,r,g,b) for xi in range(x) for yi in [0,y-1]] + [(xi,yi,100,100,100) for yi in range(y) for xi in [0,x-1]]
	set_hline([0,3],100,100,100)
	set_vline([0,7],100,100,100)

#	[uh.set_pixel(boarder[i][0],boarder[i][1],boarder[i][2],boarder[i][3],boarder[i][4]) for i in range(len(boarder))]
#	uh.show()
	time.sleep(.5)

def set_hline(col,r,g,b):
	line_ = [(xi,yi,r,g,b) for xi in range(x) for yi in col]
	[uh.set_pixel(line_[i][0],line_[i][1],line_[i][2],line_[i][3],line_[i][4]) for i in range(len(line_))]
	uh.show()

def set_vline(row,r,g,b):
	line_ = [(xi,yi,r,g,b) for yi in range(y) for xi in row]
	[uh.set_pixel(line_[i][0],line_[i][1],line_[i][2],line_[i][3],line_[i][4]) for i in range(len(line_))]
	uh.show()

print (x,y)


grid_size = (x,y)

x_mid = x // 2  # midpoint
y_mid = y // 2  # midpoint


def random_start():
	return (random.randint(0,x-1),random.randint(0,y-1))


#print ('starting point :' + str(x_pos),str(y_pos))


nsteps = 2000
hinc = 1/nsteps

def random_color():
	r = random.randint(50,250)
	g = random.randint(50,250)
	b = random.randint(50,250)
	return (r,g,b)

def color_inc(r,g,b):
	r = (r + random.randint(5,30)) % 255
	g = (g + random.randint(5,30)) % 255
	b = (b + random.randint(5,30)) % 255
	return (r,g,b)

def color_dec(r,g,b):
        r = (r - random.randint(5,30)) % 255
        g = (g - random.randint(5,30)) % 255
        b = (b - random.randint(5,30)) % 255
        return (r,g,b)

def color_chg(r,g,b):
	rnd_ = random.randint(-1,1)

	if rnd_ == -1:
		return color_dec(r,g,b)
	elif rnd_ == 1:
		return color_inc(r,g,b)
	else:
		return (r,g,b)


x_pos,y_pos = random_start()
x2,y2 = random_start()
x3,y3 = random_start()


print ('starting point :' + str(x_pos),str(y_pos))
#print ('starting point :' + str(x2),str(y2))
#print ('starting point :' + str(x3),str(y3))

def step_forward(x_pos,y_pos):
	print ('forward step')
	x_ = int(x_pos)
	y_ = int(y_pos)
	print ('positions: \n')
	print (x_,y_)
	print ('\n')
	while True:
		dx,dy = random.choice(moves)
		print ('moves')
		print(dx,dy)
		print('\n')
		if (x_ + dx) < x and (x_ + dx) >= 0 and (y_ + dy) < y and (y_ + dy) >=0:
			return (int(x_ + dx), int(y_ + dy))
		else:
			print ('hit boarder!')
			set_boarder(0,75,75)
			if random.randint(0,3) == 1:
				return (x_mid,y_mid)
			elif random.randint(0,3) == 2:
				return (x_mid-1,y_mid-1)
			elif random.randint(0,3) == 3:
				return (x_mid,y_mid-1)
			else:
				return (x_mid-1,y_mid)
			#return (x_,y_)


RGB = random_color()

for i in range(nsteps):
	uh.set_all(0,0,0)

	RGB = color_chg(RGB[0],RGB[1],RGB[2])
	set_boarder(RGB[0],RGB[1],RGB[2])

	uh.set_pixel(x_pos,y_pos,RGB[0],RGB[1],RGB[2])
#	uh.set_pixel(x2,y2,RGB[1],RGB[2],RGB[0])
#	uh.set_pixel(x3,y3,RGB[2],RGB[0],RGB[1])
	uh.show()
	
	time.sleep(.5)#,500)/100)
	
	x_pos,y_pos = step_forward(int(x_pos),int(y_pos))
#	x2,y2 = step_forward(x2,y2)
#	x3,y3 = step_forward(x3,y3)
	

	if i % 50 == 0:
		RGB = random_color()
		uh.set_all(random_color()[0],random_color()[1],random_color()[2])
		uh.show()
		time.sleep(random.randint(1,50)/100)
