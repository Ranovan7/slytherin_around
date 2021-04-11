import nimporter
import time
from nimrod import nim_math


def looper(n: int):
    result = []
    for i in range(n):
        result.append((i+1)*2)

    return result


def try_nim():
    print(nim_math.add(2, 4))

    nim_seq = nim_math.seq_int()

    print(type(nim_seq))
    print(nim_seq)
    print()

    n_fib = 5000000

    start = time.time()
    nim_fib = nim_math.looper(n_fib)
    print(f"Results using Nim : {len(nim_fib)}")
    print(f"-- execution time : {round(time.time() - start, 3)} seconds\n")

    start = time.time()
    py_fib = looper(n_fib)
    print(f"Results using Python : {len(py_fib)}")
    print(f"-- execution time : {round(time.time() - start, 3)} seconds\n")
