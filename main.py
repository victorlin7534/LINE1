from display import *
from draw import *
import math

screen, color = new_screen(), [255,0,0]

def line(i,x,y):
	draw_line(int(75*math.cos(i)+250),int(75*math.sin(i)+250),x,y,screen,color)

for i in range(500):
	if i < 125:
		line(i,int(25*math.cos(i)+125),int(25*math.sin(i)+375))
	elif i < 250:
		line(i,int(25*math.cos(i)+375),int(25*math.sin(i)+375))
	elif i < 375:
		line(i,int(25*math.cos(i)+125),int(25*math.sin(i)+125))
	else:
		line(i,int(25*math.cos(i)+375),int(25*math.sin(i)+125))
# draw_line(0,0,500,500,screen,color)
# draw_line(0,500,500,0,screen,color)
# draw_line(0,250,500,250,screen,color)
# draw_line(250,0,250,500,screen,color)

display(screen)
save_extension(screen,'img.png')
