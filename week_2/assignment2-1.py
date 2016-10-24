file = open("QuickSort.txt")
arr = [];
for line in file :
  arr.append(int(line))
file.close()

def quickSortFirst(l, r):
    # length of array
    n = r - l + 1
    # base case
    if n == 0:
        return 0;
    # partition subroutine
    # use 1st element as pivot
    pivot = arr[l];
    i = l+1
    for j in range(l+1,r+1):
        if arr[j] < pivot:
            # swap A[i], A[j]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    # recursion & return the sum of comparisons
    left_of_pivot = quickSortFirst(l,i-2)
    right_of_pivot = quickSortFirst(i, r)
    return (n - 1) + left_of_pivot + right_of_pivot

# arr = [6,2,8,3,1,9,5] # test case
m = quickSortFirst(0, len(arr)-1)
print m
# 162085
