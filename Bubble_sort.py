from Generate_random_seq import gen_random_input
import time

def bubble_sort(inp_array):
    N=len(inp_array)
    for i in range (N):
        swap = False
        for j in range (N-i-1):
            if inp_array[j]>inp_array[j+1]:
                temp = inp_array[j]
                inp_array[j] = inp_array[j+1]
                inp_array[j+1] = temp
                swap = True
        if swap == False:
            break
    return inp_array