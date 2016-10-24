file = open("IntegerArray.txt")
arr = [];
for line in file :
  arr.append(int(line))
file.close()

def inversions(arr):
    n = len(arr)

    # base case
    if n == 1:
        return (arr, 0);

    # recursion
    (sorted_left, inversions_left) = inversions(arr[0:n/2])
    (sorted_right, inversions_right) = inversions(arr[n/2:])

    # merge
    sorted_all = []
    inversions_all = 0
    while len(sorted_left) > 0 or len(sorted_right) > 0:
        if len(sorted_left) == 0:
            sorted_all += sorted_right
            sorted_right = []
        elif len(sorted_right) == 0:
            sorted_all += sorted_left
            sorted_left = []
        elif (sorted_left[0] < sorted_right[0]):
            sorted_all.append(sorted_left.pop(0))
        else:
            sorted_all.append(sorted_right.pop(0))
            inversions_all += len(sorted_left)
    return (sorted_all, inversions_left + inversions_right + inversions_all)

# arr = [6,2,8,3,1,9,5] test case
# (sorted_all, inversions_all) = inversions(arr)

import time
start = time.time()
(sorted_all, inversions_all) = inversions(arr)
print(inversions_all)
print("RUNTIME = " + str(time.time() - start))
