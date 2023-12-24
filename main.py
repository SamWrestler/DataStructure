import random
import time
import matplotlib.pyplot as plt

def make_array(size):
    return list(range(size))

def remove_from_array(int, array):
    array.remove(int)
    return array

def print_execution_times(times):
    for time_val in times:
        print(time_val)

def draw_graph(x, y):
    plt.plot(x, y, marker='o', linestyle='-')

    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Array Size')
    plt.show()



def linear_search():
    exetimes = []
    array_length = []

    for i in range(5):
        array_size = 10 * 10**i
        array_length.append(array_size)

        #   Make array using make_array function
        array = make_array(array_size)

        #   Make a none excisted target
        target = 10 * 10**i


        #   Calculating the execution time
        start_time = time.time()
        found = False

        for z in array:
            if z == target:
                found = True
                break
            time.sleep(0.0000001)

        end_time = time.time()
        result = end_time - start_time

        #   Append calculated times to an array called exetimes
        exetimes.append(result)

        if found:
            print("Found")
        else:
            print("Not found")

    #   Function to print out execution times into console
    print_execution_times(exetimes)

    #   Function to draw execution times on a graph
    draw_graph(array_length, exetimes)

def binary_search():
    exetimes = []
    array_length = []
    array_size = [10,100,1000,10000,100000,1000000,10000000,100000000]
    for i in array_size:
        target = 3 
        array = make_array(i)
        array = remove_from_array(target, array)

        array_length.append(i)

        start_time = time.time()
        high = len(array) - 1
        low = 0
        while(low <= high):
            mid = (low + high)//2
            mid_value = array[mid]
            if (mid_value > target):
                time.sleep(0.1)
                high = mid - 1
            elif (mid_value < target):
                time.sleep(0.1)
                low = mid + 1
            else:
                time.sleep(0.1)
                return mid

        end_time = time.time()

        result = end_time - start_time
        exetimes.append(result)
        
    print_execution_times(exetimes)
    draw_graph(array_length, exetimes)

binary_search()