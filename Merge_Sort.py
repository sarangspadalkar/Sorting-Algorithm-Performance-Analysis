from Generate_random_seq import gen_random_input
import time

def merge_sort(inp_array):
    N=len(inp_array)
    if N > 1:
        middle = N//2
        left_arr = inp_array[:middle]
        right_arr = inp_array[middle:]
        merge_sort (left_arr)
        merge_sort (right_arr)
        
        k=left_index=right_index=0
        while left_index < len (left_arr) and right_index < len (right_arr):
            if left_arr[left_index] < right_arr[right_index] :
                inp_array[k] = left_arr[left_index]
                left_index +=1
            else :
                inp_array[k] = right_arr[right_index]
                right_index+=1
            k+=1
        while left_index < len(left_arr):
            inp_array[k] = left_arr[left_index]
            left_index+=1
            k+=1
        
        while right_index < len(right_arr):
            inp_array[k] = right_arr[right_index]
            right_index+=1
            k+=1
    return inp_array