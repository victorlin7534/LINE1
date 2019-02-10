from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	x0, x1 = x1 if x1<x0 else x0, x0 if x1<x0 else x1
	y0, y1 = y1 if x1<x0 else y0, y0 if x1<x0 else y1
	a = y1-y0
	b = x0-x1
	m = (y1-y0)/(x1-x0) if (x1-x0) != 0 else 2
	if m > 1:#q2
		d = a + 2*b
		while y0 <= y1:
			plot(screen,color,x0,y0)
			if d < 0:
				x0+=1
				d += 2*a
			y0+=1
			d += 2*b
	elif m > 0:#q1
		d = 2*a + b
		while x0 <= x1:
			plot(screen,color,x0,y0)
			if d > 0:
				y0+=1
				d += 2*b
			x0+=1
			d += 2*a
	elif m > -1:#q8
		d = 2*a -b		
		while x0 <= x1:
			plot(screen,color,x0,y0)
			if d < 0:
				y0-=1
				d -= 2*b
			x0+=1
			d += 2*a
	else:#q7
		d = a - 2*b
		while y0 >= y1:
			plot(screen,color,x0,y0)
			if d > 0:
				x0+=1
				d += 2*a
			y0-=1
			d -= 2*b 
