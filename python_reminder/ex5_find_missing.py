# --------------------------------------------------------------------------
# EXERCISE 5: A sorted array (A) of length N is populated with
# N consecutive different integers ranging from 0 to N with
# one number always missing.
#
# For example, if N=7 and the array = [0,1,2,3,4,6,7] then the missing
# value is 5  or if the array = [1,2,3,4,5,6,7] then the missing value
# is 0. Provide the code for an algorithm that finds and prints out the
# missing integer.
#
# What is the big O of your code? Can you find an O(logn) algorithm?
# --------------------------------------------------------------------------

# Find mid point, then only check either left or right subset


def find_missing(arr):
    for i in range(len(arr)):
        if arr[i] != i:
            return i


def find_missing_improved(arr):
    mid_point = len(arr) // 2
    if arr[mid_point] == mid_point:
        for i in range(mid_point + 1, len(arr)):
            if arr[i] != i:
                return i
    else:
        for i in range(mid_point + 1):
            if arr[i] != i:
                return i


print(find_missing([0, 1, 2, 3, 4, 6, 7]))
print(find_missing([1, 2, 3, 4, 5, 6, 7]))
