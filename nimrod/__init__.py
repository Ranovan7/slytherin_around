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


def try_3d_gif():
    # Fixing random state for reproducibility
    np.random.seed(19680801)


    def Gen_RandLine(length, dims=2):
        """
        Create a line using a random walk algorithm

        length is the number of points for the line.
        dims is the number of dimensions the line has.
        """
        lineData = np.empty((dims, length))
        lineData[:, 0] = np.random.rand(dims)
        for index in range(1, length):
            # scaling the random numbers by 0.1 so
            # movement is small compared to position.
            # subtraction by 0.5 is to change the range to [-0.5, 0.5]
            # to allow a line to move backwards.
            step = ((np.random.rand(dims) - 0.5) * 0.1)
            lineData[:, index] = lineData[:, index - 1] + step

        return lineData


    def update_lines(num, dataLines, lines):
        for line, data in zip(lines, dataLines):
            # NOTE: there is no .set_data() for 3 dim data...
            line.set_data(data[0:2, :num])
            line.set_3d_properties(data[2, :num])
        return lines

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # Fifty lines of random 3-D lines
    data = [Gen_RandLine(25, 3) for index in range(50)]

    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

    # Setting the axes properties
    ax.set_xlim3d([0.0, 1.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 1.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 1.0])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                                       interval=50, blit=False)

    plt.show()


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
