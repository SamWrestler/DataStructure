import random
import time
import matplotlib.pyplot as plt

def linear_search():
    exetimes = []
    array_length = []

    for i in range(5):
        array_size = 10 * 10**i
        array_length.append(array_size)
        array = make_array(array_size)
        target = 10 * 10**i

        start_time = time.time()
        found = False

        for z in array:
            if z == target:
                found = True
                break
            time.sleep(0.0000001)

        end_time = time.time()
        result = end_time - start_time

        exetimes.append(result)

        if found:
            print("Found")
        else:
            print("Not found")

    print_execution_times(exetimes)
    draw_graph(array_length, exetimes)

def binary_search():
    exetimes = []
    array_length = []

    for i in range(5):
        array_size = 10 * 10**i
        array_length.append(array_size)
        array = make_array(array_size)
        target = 10 * 10**i

        start_time = time.time()
        found = False

        for z in array:
            if z == target:
                found = True
                break
            time.sleep(0.0000001)

        end_time = time.time()
        result = end_time - start_time

        exetimes.append(result)

        if found:
            print("Found")
        else:
            print("Not found")

    print_execution_times(exetimes)
    draw_graph(array_length, exetimes)

def make_array(size):
    return list(range(size))

def print_execution_times(times):
    for time_val in times:
        print(time_val)

def draw_graph(x, y):
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Array Size')
    plt.show()

linear_search()
