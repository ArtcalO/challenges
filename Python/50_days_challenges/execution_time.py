import time

def execution_time(func, *args, **kwargs):
    start_time = time.time() 
    result = func(**kwargs)
    end_time = time.time() 
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time:.6f} seconds")
    print(result) 