# Author: Mahtab Zilaie
# Date: February 26 2020
# Description: sort_timer_decorator function returns time elapsed from a bubble sort and insertion sort
# and a list is generated of time elapsed for both sort functions to return a list, compare_sorts
# function produces a graph from lists

import time
import random


def sort_timer_decorator(func):
    """decorator function checks start time/end time of function and returns time elapsed"""
    def sort_time(*args, **kwargs):
        start_time = time.perf_counter()   # records start time of function
        func(*args, **kwargs)
        end_time = time.perf_counter()     # records end time of function
        return (end_time - start_time)     # returns time elapsed

    return sort_time


@sort_timer_decorator
def bubble_sort(a_list):
    """
  Sorts a_list in ascending order
  """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer_decorator
def insertion_sort(a_list):
    """
  Sorts a_list in ascending order
  """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def generateList(size):
    """ generates a list from random integers 1-10000"""
    retList = []
    for i in range(size):
        retList.append(random.randint(1, 10000))    # produces random numbers 1-10000 and adds to list
    return retList                                 # returns list


def compare_sorts(sort_func1, sort_func2):           # compares two functions
    """ compares two functions and produces a list from time elapsed and creates a graph based off data"""
    timeList1 = []
    timeList2 = []
    for length in range(1000, 10001, 1000):        # starts at 1000-10000, for every 1000
        list_1 = generateList(length)            # creates a list from random
        list_2 = list(list_1)                   # copies list
        timeList1.append(sort_func1(list_1))   # adds time elapsed from sort function to list
        timeList2.append(sort_func2(list_2))
    # plot graph
    from matplotlib import pyplot
    pyplot.plot(timeList1, timeList2, 'ro--', linewidth=2)  # x-coord is from timeList1, y-coord from timelist2
    pyplot.title("Sorting Time series comparision")
    pyplot.xlabel("Bubble Sort")
    pyplot.ylabel("Insertion Sort")
    pyplot.show()                                           # shows graph


compare_sorts(bubble_sort, insertion_sort)          # bubble_sort is sort_func1, insertion_sort is sort_func2
