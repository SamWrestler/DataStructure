import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Button, messagebox
import threading
import random

# A function to make arrays in given sizes
def make_array(size):
    return list(range(size))

# This function remove on value from the given array (specially for worst case scenario in binary search)
def remove_from_array(val, array):
    array.remove(val)
    return array

# This function calculate the execution times
def print_execution_times(times):
    for time_val in times:
        print(time_val)

# This function draw the graph
def draw_graph(x, y, title):
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title(title)
    plt.show()

# Linear search function
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
    draw_graph(array_length, exetimes, 'Linear Search Execution Time vs. Array Size')

# Binary search function
def binary_search():
    exetimes = []
    array_length = []
    array_size = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

    for i in array_size:
        target = 3
        array = make_array(i)
        array = remove_from_array(target, array)

        array_length.append(i)

        start_time = time.time()
        high = len(array) - 1
        low = 0

        while low <= high:
            mid = (low + high) // 2
            mid_value = array[mid]

            if mid_value > target:
                time.sleep(0.1)
                high = mid - 1
            elif mid_value < target:
                time.sleep(0.1)
                low = mid + 1
            else:
                time.sleep(0.1)
                return mid

        end_time = time.time()
        result = end_time - start_time
        exetimes.append(result)

    print_execution_times(exetimes)
    draw_graph(array_length, exetimes, 'Binary Search Execution Time vs. Array Size')

# Bubble sort alg function to make the algorithm
def bubble_sort_alg(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Bubble sort function to calculate the execution times and pass the variables into draw_graph function
def bubble_sort():
    exetimes = []
    array_length = [10, 100, 1000, 10000, 20000, 30000, 40000, 50000]  # Adjust as needed

    for size in array_length:
        array = make_array(size)

        start_time = time.time()
        bubble_sort_alg(array)
        end_time = time.time()

        result = end_time - start_time
        exetimes.append(result)

    print_execution_times(exetimes)
    draw_graph(array_length, exetimes, 'Bubble Sort Execution Time vs. Array Size')

# Quick sort alg function to make the algorithm
def quick_sort_alg(arr):    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_alg(less) + [pivot] + quick_sort_alg(greater)

# Quick sort function to calculate the execution times and pass the variables into draw_graph function
def quick_sort():
    exetimes = []
    array_length = [1000, 10000, 100000, 1000000, 2000000, 3000000,4000000,5000000,6000000,7000000]  # Adjust as needed

    for size in array_length:
        array = make_array(size)
        random.shuffle(array)  

        start_time = time.time()
        quick_sort_alg(array)
        end_time = time.time()

        result = end_time - start_time
        exetimes.append(result)
    print_execution_times(exetimes)
    draw_graph(array_length, exetimes, 'Quick Sort Execution Time vs. Array Size')

# Function to make honi tower in different sizes
def hanoi_tower(n, source_peg, target_peg, auxiliary_peg):
    if n > 0:
        hanoi_tower(n-1, source_peg, auxiliary_peg, target_peg)
        time.sleep(0.0000001)
        hanoi_tower(n-1, auxiliary_peg, target_peg, source_peg)
        time.sleep(0.00001)

# Calculate the execution times
def hanoi():
    exetimes = []
    array_length = [3, 4, 5, 6, 7, 8, 9, 10]  

    for size in array_length:
        start_time = time.time()
        hanoi_tower(size, 'A', 'C', 'B')
        end_time = time.time()

        result = end_time - start_time
        exetimes.append(result)
        print(result)
    print_execution_times(exetimes)
    draw_graph(array_length, exetimes, 'Tower of Hanoi Execution Time vs. Number of Discs')


# a class to make gui for the project using tkinter library
class SortingApp:
    def __init__(self, master):
        self.master = master
        master.title("Sorting Algorithm App")
        master.geometry("500x350")

        self.colors = ["#2ecc71", "#3498db", "#34495e", "#f1c40f", "#e74c3c"]

        label_text = """Dear Mr. Vaziri,

I have developed the following program using the Python programming language. This program evaluates the execution time of 5 different algorithms at various scales and generates corresponding charts using the Matplotlib library."""

        self.label = tk.Label(self.master, text=label_text, justify=tk.LEFT, wraplength=450)
        self.label.pack(pady=10)

        self.linear_search_button = self.create_button("Linear Search", self.linear_search, self.colors[0])
        self.binary_search_button = self.create_button("Binary Search", self.binary_search, self.colors[1])
        self.bubble_sort_button = self.create_button("Bubble Sort", self.bubble_sort, self.colors[2])
        self.quick_sort_button = self.create_button("Quick Sort", self.quick_sort, self.colors[3])
        self.hanoi_button = self.create_button("Tower of Hanoi", self.hanoi, self.colors[4])

    def create_button(self, text, command, color):
        button = Button(self.master, text=text, command=lambda: self.run_algorithm(command), bg=color, width=20, height=2)
        button.pack(pady=5)
        return button

    def run_algorithm(self, command):
        dialog = tk.Toplevel(self.master)
        dialog.title("Please Wait")
        dialog.geometry("200x100")
        label = tk.Label(dialog, text="Running...\nPlease wait.")
        label.pack(pady=20)

        thread = threading.Thread(target=self.run_with_dialog, args=(command, dialog))
        thread.start()

    def run_with_dialog(self, command, dialog):
        command()
        dialog.destroy()
        messagebox.showinfo("Done", "Algorithm completed!")

    def linear_search(self):
        self.simulate_processing()
        print("Linear Search")
        linear_search()

    def binary_search(self):
        self.simulate_processing()
        print("Binary Search")
        binary_search()
        
    def bubble_sort(self):
        self.simulate_processing()
        print("Bubble Sort")
        bubble_sort()
        
    def quick_sort(self):
        self.simulate_processing()
        print("Quick Sort")
        quick_sort()

    def hanoi(self):
        self.simulate_processing()
        print("Tower of Hanoi")
        hanoi()
        
    def simulate_processing(self):
        time.sleep(2)

root = tk.Tk()
app = SortingApp(root)
root.mainloop()
