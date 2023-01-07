import schedule
import time
import datetime


def func():
    print("Geeksforgeeks")
    time = datetime.datetime.now()
    display_time = time.strftime("%H:%M")
    print(display_time)

schedule.every(7).seconds.do(func)

while True:
	schedule.run_pending()
    
	time.sleep(3)
