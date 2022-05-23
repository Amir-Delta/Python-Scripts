# This scrip defines a function named sorter() which takes as input a list of numerics and sorts its values

# importing packages
import numpy as np

# defining the function
def ListSorter(l):
    sorted=[]
    for i in np.arange(len(l)):
        minimum=min(l)
        minimum_index=l.index(minimum)
        l.pop(minimum_index)
        sorted.append(minimum)
    return sorted

# testing the function on a list
List= [5 , 9, 0.25, 1/3, 5 , 10 , 1 , 1 , 4 , 0.4]
print(ListSorter(List))





