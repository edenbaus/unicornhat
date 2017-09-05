import os
import time
import random
import unicornhat as uh

uh.set_layout(uh.AUTO)
uh.brightness(0.45)
x,y = uh.get_shape()
x_mid,y_mid = uh.get_shape()[0] // 2, uh.get_shape()[1] // 2

def set_hline(col,r,g,b):
        line_ = [(xi,yi,r,g,b) for xi in range(x) for yi in col]
        [uh.set_pixel(line_[i][0],line_[i][1],line_[i][2],line_[i][3],line_[i][4]) for i in range(len(line_))]
        uh.show()
        
def set_hpline(col,rows,r,g,b):
        line_ = [(xi,yi,r,g,b) for xi in range(rows) for yi in col]
        [uh.set_pixel(line_[i][0],line_[i][1],line_[i][2],line_[i][3],line_[i][4]) for i in range(len(line_))]
        uh.show()

def set_vline(row,r,g,b):
        line_ = [(xi,yi,r,g,b) for yi in range(y) for xi in row]
        [uh.set_pixel(line_[i][0],line_[i][1],line_[i][2],line_[i][3],line_[i][4]) for i in range(len(line_))]
        uh.show()
        
def set_boarder(r,g,b):
        x,y = uh.get_shape()
        set_hline([0,y-1],r,g,b)
        set_vline([0,x-1],r,g,b)
        time.sleep(.1)
        
def random_start():
        return (random.randint(0,x-1),random.randint(0,y-1))

def random_color():
        r = random.randint(50,250)
        g = random.randint(50,250)
        b = random.randint(50,250)
        time.sleep(.02)
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

def colorinc_r(r,g,b,magnitude): #magnitude is % change ie: 5 -> 5% increase
    try:
        return (int(r* (1 + magnitude/100) % 255),g,b)
    except:
        print ('Magnitude error!')

def colorinc_g(r,g,b,magnitude):
    try:
        return (r,int(g*(1 + magnitude/100)% 255),b)
    except:
        print ('Magnitude error!')
        
def colorinc_b(r,g,b,magnitude):
    try:
        return (r,g,int(b*(1 + magnitude/100) % 255))
    except:
        print ('Magnitude error!')
        
def colordec_r(r,g,b,magnitude):
    try:
        return (int(r*(1 - magnitude/100) % 255),g,b)
    except:
        print ('Magnitude error!')
        
def colordec_g(r,g,b,magnitude):
    try:
        return (r,int(g*(1 - magnitude/100) % 255),b)
    except:
        print ('Magnitude error!')
        
def colordec_b(r,g,b,magnitude):
    try:
        return (r,g,int(b*(1 - magnitude/100) % 255))
    except:
        print ('Magnitude error!')
        
def RGB_chg(RGBcomponent,magnitude):
    try:
        return max(int(RGBcomponent * (1 + magnitude/100) % 255),110)
    except:
        print ('Magnitude error! \n-\n or RGB error!')
            

def set_scale_hline(col,r_start,g_start,b_start,magnitude_r,magnitude_g,magnitude_b):
    r_ = r_start
    g_ = g_start
    b_ = b_start
    for i in range(uh.get_shape()[1]):
        uh.set_pixel(col,i,r_,g_,b_)
        uh.show()
        time.sleep(.2)
        r_ = RGB_chg(r_,magnitude_r)
        g_ = RGB_chg(g_,magnitude_g)
        b_ = RGB_chg(b_,magnitude_b)  
    
def set_scale_vline(row,r_start,g_start,b_start,magnitude_r,magnitude_g,magnitude_b):
    r_ = r_start
    g_ = g_start
    b_ = b_start
    for i in range(uh.get_shape()[0]):
        uh.set_pixel(i,row,r_,g_,b_)
        uh.show()
        time.sleep(.2)
        r_ = RGB_chg(r_,magnitude_r)
        g_ = RGB_chg(g_,magnitude_g)
        b_ = RGB_chg(b_,magnitude_b)            
        
def set_c_boarder(r,g,b):
    x,y = uh.get_shape()
    set_hline([0,y-1],r,g,b)
    set_vline([0,x-1],r,g,b)
    time.sleep(.1)

def random_gridfill():
    RGB=random_color()
    set_scale_vline(0,RGB[0],RGB[1],RGB[2],25,0,0)
    set_scale_vline(1,RGB[0],RGB[2],RGB[1],25,25,0)
    set_scale_vline(2,RGB[1],RGB[0],RGB[2],25,25,25)
    set_scale_vline(3,RGB[1],RGB[2],RGB[0],50,25,25)

            
def uh_reset():
    uh.clear()
    uh.show()