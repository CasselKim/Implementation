import time

def playtime(func) : 
    def wrapper(*args, **kwargs) : 
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time()-start)
        return res
    return wrapper
