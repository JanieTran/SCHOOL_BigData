# --------------------------------------------------------------------------
# EXERCISE 4: An array A of length n contains a random mix of positive and
# negative integers.  Describe an O(n) algorithm that rearranges these
# integers so that the negative integers appear before the positive integer.
#
# You may use additional variables as indices or for storing temporary
# values, but no additional arrays can be allocated or used.
# --------------------------------------------------------------------------


def rearrange_neg_pos(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < 0 <= arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                break

    return arr


print(rearrange_neg_pos([9, -9, 2, 4, -3, -1]))
