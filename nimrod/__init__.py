import nimporter
import time
from nimrod import nim_math


def looper(n: int):
    result = []
    for i in range(n):
        result.append((i+1)*2)

    return result[n-10:]


def looper_str(text: str, subtext:str, n_iter: int):
    for i in range(n_iter):
        subtext in text


def try_nim():
    print(nim_math.add(2, 4))

    nim_seq = nim_math.seq_int()

    print(type(nim_seq))
    print(nim_seq)
    print()

    n_fib = 50_000_000

    start = time.time()
    nim_fib = nim_math.looper(n_fib)
    print(f"Results using Nim : {len(nim_fib)}")
    print(f"-- execution time : {round(time.time() - start, 3)} seconds\n")

    start = time.time()
    py_fib = looper(n_fib)
    print(f"Results using Python : {len(py_fib)}")
    print(f"-- execution time : {round(time.time() - start, 3)} seconds\n")

    text = '''
I think this very thing is not like the thing that I think it is
I would be happy to eat a banana collected from an apple tree, though I am not really sure
it would taste like a banana - rather like an apple. What's the point in eating a banana that
tastes like an apple? Or, for that matter, eating an apple that tastes like a banana?

Some day I will explain you everything in detail. Today, gotta go since I have some performance
comparisons to do. Bye!
    '''
    subtext = "gotta go since"

    n_iter = 5_000_000

    start = time.time()
    nim_fib = nim_math.looper_str(text, subtext, n_iter)
    print(f"Results using Nim")
    print(f"-- execution time : {round(time.time() - start, 3)} seconds\n")

    start = time.time()
    py_fib = looper_str(text, subtext, n_iter)
    print(f"Results using Python")
    print(f"-- execution time : {round(time.time() - start, 3)} seconds\n")
