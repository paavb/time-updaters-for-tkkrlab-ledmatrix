import os
import time

timeold = 0
while 1:
	timenew = [time.strftime('%H') ,':' ,time.strftime('%M')]
	timenew = ''.join(map(str,timenew))
	if timenew != timeold:
		os.system("wget --spider 'http://10.42.2.104/~jawsper/led.php?action=text&text=      '" + timenew)
		timeold = timenew
	time.sleep(4)