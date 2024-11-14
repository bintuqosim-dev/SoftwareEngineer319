def fibonacci_search(arr, target):
    n = len(arr)
    fib_m_2 = 0 
    fib_m_1 = 1  
    fib_m = fib_m_2 + fib_m_1  
    while fib_m < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib_m
        fib_m = fib_m_2 + fib_m_1
    offset = -1
    while fib_m > 1:   
        i = min(offset + fib_m_2, n - 1)
        if arr[i] == target:
            return i
        elif arr[i] < target:
            fib_m = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib_m - fib_m_1
            offset = i       
        else:
            fib_m = fib_m_2
            fib_m_1 = fib_m_1 - fib_m_2
            fib_m_2 = fib_m - fib_m_1  
    if fib_m_1 and arr[offset + 1] == target:
     return offset + 1
    return -1  
arr = [10, 22, 35, 40, 45, 50, 70, 80, 82, 85]
target = 45
result = fibonacci_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")
