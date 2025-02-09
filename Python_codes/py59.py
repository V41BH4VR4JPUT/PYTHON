"""
Time Module in Python

1. time.time() - returns the current time in seconds since the epoch
2. time.sleep() - suspends execution for the given number of seconds
3. time.localtime() - returns the current time in a tuple
4. time.asctime() - returns the current time in a string
5. time.strftime() - returns the current time in a string

"""
import time
 
current_time = time.time()
print(time.time() - current_time)

Before = time.time()
print(Before)
time.sleep(2)
After = time.time()
print(After)

Now = time.asctime(time.localtime(time.time()))
print(Now)

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(now)