import random
import time
import matplotlib.pyplot as plt

def linear_search():
    exetimes = []
    array_length = []
    for i in range(5):
        array_size = 10 * pow(10 , i)
        array_length.append(array_size)
        array = make_arrays(array_size)
        target = 10 * pow(10,i)
        start_time = time.time()
        for z in array:
            if z == target:
                return "Found"
            time.sleep(0.000001)

        end_time = time.time()
        result = end_time - start_time  
        exetimes.append(result)
    for k in exetimes:
        print(k)
    draw_graph(array_length, exetimes)
def make_arrays(i):
    arr = []
    for j in range(i):
        arr.append(j)
    return arr

def draw_graph(x,y):
    

    # Plotting the graph
    plt.plot(x, y, marker='o', linestyle='-')

    # Adding labels and title
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Array Size')

    # Display the graph
    plt.show()

linear_search()