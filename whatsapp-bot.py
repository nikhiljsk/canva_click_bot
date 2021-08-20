import pyautogui as pg
import time

def write_text(i):
	pg.click(1222, 1000)
	a = "Hi:"+str(i)
	pg.typewrite(a)
	pg.click(1884, 1006)
	
a=1
time.sleep(5)
for i in range(a):
	write_text(i)
