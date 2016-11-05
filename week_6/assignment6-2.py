import heapq

def load_file(file_to_open):
    file = open(file_to_open)
    lines = file.read().split('\n')
    arr = [];
    for line in lines[:-1]: # file ends with extra line break
        number = int(line)
        arr.append(number)
    file.close()
    return arr

file = "Median.txt"
arr = load_file(file)

def medians(arr):
    smaller_than_median = [] # in python, this is a -1*heapq (max heap)
    greater_than_median = [] # in python, this is a heapq (min heap)
    medians = [];
    last_median = None
    for n in arr:
        heap_difference = len(smaller_than_median) - len(greater_than_median)
        if last_median == None:
            heapq.heappush(smaller_than_median, -1*n)
        elif n < last_median:
            if heap_difference == 0:
                heapq.heappush(smaller_than_median, -1*n)
            else: # heap_difference = 1
                move_n = heapq.heappushpop(smaller_than_median, -1*n)
                heapq.heappush(greater_than_median, -1*move_n)
        else: # n > last_median
            if heap_difference == 0:
                move_n = heapq.heappushpop(greater_than_median, n)
                heapq.heappush(smaller_than_median, -1*move_n)
            else: # heap_difference = 1
                heapq.heappush(greater_than_median, n)
        median = -1*smaller_than_median[0]
        medians.append(median)
        last_median = median
    return medians

medians = medians(arr)
print sum(medians)
# 7912
