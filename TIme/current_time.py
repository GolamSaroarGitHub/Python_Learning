import time

timestamp=time.time()

current_time=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(timestamp))

print(current_time)