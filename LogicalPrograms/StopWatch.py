import time

class StopWatch:
    def __init__(self):
        self.start_point = 0

    def start(self):
            self.start_point = time.perf_counter()

    def stop(self):
       elapsed = time.perf_counter() - self.start_point
       return f"{elapsed:.2f} seconds"
    
watch=StopWatch()
watch.start()
for i in range(5000000):    pass
print(watch.stop())

  
