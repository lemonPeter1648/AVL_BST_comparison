import bst
import avl
import time
from matplotlib import pyplot as plt
import random
import gc

def creating_tree_plot_bst():
    number_of_elements_list = [100000, 150000, 200000, 250000, 300000, 350000, 400000]
    times = []
    for number in number_of_elements_list:
        list = random.sample(range(1, 3000000), number)
        root = None
        root = bst.insert(root, 15000)
        start = time.process_time()
        for element in list:
            root = bst.insert(root, element)
        end = time.process_time()
        creating_time = end - start
        times.append(creating_time)


    plt.plot(number_of_elements_list, times, label="bst")
    plt.legend()
    plt.savefig("creating_time_.png")


def searching_tree_plot_bst():
    number_of_searched_elements = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000]
    list = random.sample(range(1, 3000000), 100000)
    root = None
    root = bst.insert(root, 50000)
    searching_times = []
    for element in list:
        root = bst.insert(root, element)
    for number in number_of_searched_elements:
        start = time.process_time()
        for element in range(0, number):
            root.search(root, list[element])
        end = time.process_time()
        searching_time = end - start
        searching_times.append(searching_time)
    plt.plot(number_of_searched_elements, searching_times, label="bst")
    plt.xlabel("Number of searched elements")
    plt.ylabel("Searching times")
    plt.legend()
    plt.savefig("searching_time.png")

def removing_tree_plot_bst():
    number_of_removing_elements = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000]
    list = random.sample(range(1, 3000000), 100000)
    root = None
    root = bst.insert(root, 50000)
    removing_times = []
    for element in list:
        root = bst.insert(root, element)
    for number in number_of_removing_elements:
        start = time.process_time()
        for element in range(0, number):
            root.search(root, list[element])
        end = time.process_time()
        searching_time = end - start
        removing_times.append(searching_time)
    plt.plot(number_of_removing_elements, removing_times, label="bst")
    plt.xlabel("Number of removed elements")
    plt.ylabel("Removing times")
    plt.legend()
    plt.savefig("removing_time.png")

def creating_tree_plot_avl():
    number_of_elements_list = [100000, 150000, 200000, 250000, 300000, 350000, 400000]
    times = []
    for number in number_of_elements_list:
        list = random.sample(range(1, 3000000), number)
        myTree = avl.AVLTree()
        root = None
        root = myTree.insert_node(root, 15000)
        start = time.process_time()
        for element in list:
            root = myTree.insert_node(root, element)
        end = time.process_time()
        creating_time = end - start
        times.append(creating_time)

    plt.plot(number_of_elements_list, times, label="avl")
    plt.xlabel("Number of elements")
    plt.ylabel("Time of tree creating")
    plt.legend()

def searching_tree_plot_avl():
    number_of_searched_elements = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000]
    list = random.sample(range(1, 3000000), 100000)
    root = None
    mytree = avl.AVLTree()
    root = mytree.insert_node(root, 45000)
    searching_times = []
    for element in list:
        root = mytree.insert_node(root, element)
    for number in number_of_searched_elements:
        start = time.process_time()
        for element in range(0, number):
            mytree.search(root, list[element])
        end = time.process_time()
        searching_time = end - start
        searching_times.append(searching_time)
    plt.plot(number_of_searched_elements, searching_times, label="avl")
    plt.xlabel("Number of searched elements")
    plt.ylabel("Searching times")


def removing_tree_plot_avl():
    number_of_removing_elements = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000]
    list = random.sample(range(1, 3000000), 100000)
    root = None
    mytree = avl.AVLTree()
    root = mytree.insert_node(root, 50000)
    removing_times = []
    for element in list:
        root = mytree.insert_node(root, element)
    for number in number_of_removing_elements:
        start = time.process_time()
        for element in range(0, number):
            mytree.delete_node(root, list[element])
        end = time.process_time()
        searching_time = end - start
        removing_times.append(searching_time)
    plt.plot(number_of_removing_elements, removing_times, label="avl")
    plt.xlabel("Number of removed elements")
    plt.ylabel("Removing times")

if __name__ == "__main__":
    gc.disable()
    creating_tree_plot_avl()
    creating_tree_plot_bst()
    plt.cla()

    searching_tree_plot_avl()
    searching_tree_plot_bst()
    plt.cla()

    removing_tree_plot_avl()
    removing_tree_plot_bst()