import time

def playtime(func) : 
    def wrapper() : 
        start = time.time()
        func()
        print(time.time()-start)
    return wrapper
