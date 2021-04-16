import nimporter
import time
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from nimrod import nim_math


def looper(n: int):
    result = []
    for i in range(n):
        result.append((i+1)*2)

    return result[n-10:]


def looper_str(text: str, subtext:str, n_iter: int):
    for i in range(n_iter):
        subtext in text


def generate_data(nbr_iterations, nbr_elements):
    dims = (3,1)

    # Random initial positions.
    gaussian_mean = np.zeros(dims)
    gaussian_std = np.ones(dims)
    start_positions = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [nbr_elements] * dims[0]))).T

    # Random speed
    start_speed = np.array(list(map(np.random.normal, gaussian_mean, gaussian_std, [nbr_elements] * dims[0]))).T

    # Computing trajectory
    data = [start_positions]
    for iteration in range(nbr_iterations):
        previous_positions = data[-1]
        new_positions = previous_positions + start_speed
        data.append(new_positions)

    return data

def animate_scatters(iteration, data, scatters):
    for i in range(data[0].shape[0]):
        scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,1:2], data[iteration][i,2:])
    return scatters

def animate_3d(data):
    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    print(len(data))

    # Initialize scatters
    scatters = [ ax.scatter(data[0][i,0:1], data[0][i,1:2], data[0][i,2:]) for i in range(data[0].shape[0]) ]

    # Number of iterations
    iterations = len(data)

    # Setting the axes properties
    ax.set_xlim3d([-50, 50])
    ax.set_xlabel('X')

    ax.set_ylim3d([-50, 50])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-50, 50])
    ax.set_zlabel('Z')

    ax.set_title('3D Animated Scatter Example')

    # Provide starting angle for the view.
    ax.view_init(25, 10)

    ani = animation.FuncAnimation(fig, animate_scatters, iterations, fargs=(data, scatters),
                                       interval=50, blit=False, repeat=True)

    plt.show()


def try_3d_gif():
    data = generate_data(100, 2)
    animate_3d(data)


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
