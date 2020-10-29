import schedule
import time

def x():
    print("Hello World")

def y():
    print("Python 3.8")

schedule.every(5).seconds.do(x)
schedule.every(15).seconds.do(y)

while True:
    schedule.run_pending()
    time.sleep(1)
