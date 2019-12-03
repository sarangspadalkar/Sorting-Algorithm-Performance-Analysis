from Bubble_sort import bubble_sort
from Insertion_sort import insertion_sort
from Merge_Sort import merge_sort
from Generate_random_seq import gen_random_input
from Selection_sort import selection_sort
import time
import pandas as pd
import matplotlib.pyplot as plt
final_sort_dict_avg={}
final_sort_dict_best={}
final_sort_dict_worst={}
for sort in ['bubble','insertion','merge','selection']:
    time_dict_best={}
    time_dict_worst={}
    time_dict_average={}
    for str in ['best','worst','average']:
        for i in range(100,1000,100):
            inp_array=gen_random_input(str,i)
            duration=[]    
            for j in range (1,10):
                start_time=time.time_ns()
                if sort == 'merge':
                    merge_sort(inp_array)
                    duration.append(time.time_ns()-start_time)
                elif sort == 'insertion':
                    insertion_sort(inp_array)
                    duration.append(time.time_ns()-start_time)
                elif sort == 'bubble':
                    bubble_sort(inp_array)
                    duration.append(time.time_ns()-start_time)
                else:
                    selection_sort(inp_array)
                    duration.append(time.time_ns()-start_time)
            average_time= sum(duration)/len(duration)
            if str == 'best':
                time_dict_best[i] = average_time
            elif str == 'worst':
                time_dict_worst[i] = average_time
            else :
                time_dict_average[i] = average_time
    final_sort_dict_best[sort]=list(time_dict_best.values())
    final_sort_dict_worst[sort]=list(time_dict_worst.values())
    final_sort_dict_avg[sort]=list(time_dict_average.values())
print ("\nBest Time:",final_sort_dict_best,"\n\nWorst Time:",final_sort_dict_worst,"\n\nAverage Time:",final_sort_dict_avg)

df_best_time=pd.DataFrame(final_sort_dict_best)
df_worst_time=pd.DataFrame(final_sort_dict_worst)
df_avg_time=pd.DataFrame(final_sort_dict_avg)
df_best_time["input_length"]=[i for i in range(100,1000,100)]
df_worst_time["input_length"]=[i for i in range(100,1000,100)]
df_avg_time["input_length"]=[i for i in range(100,1000,100)]
df_best_time.set_index('input_length',inplace=True)
df_worst_time.set_index('input_length',inplace=True)
df_avg_time.set_index('input_length',inplace=True)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(15,5))
df_best_time.plot(title="Best Case Analysis",ax=ax1,marker='s')
df_worst_time.plot(title= "Worst Case Analysis",ax=ax2,marker='s')
df_avg_time.plot(title="Average Case Analysis",ax=ax3,marker='s')
    