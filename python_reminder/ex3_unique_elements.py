# --------------------------------------------------------------------------
# EXERCISE 3: Write a Python function that takes a list and
# prints out the unique elements of the list.
#
# For example, if the list is [10,6,7,4,6,8,9,7,11,10],
# the output will be the values [11,10,6,4,7,8,9].
# Note that the order of the output is not important.
# What is the big O of your code?
# --------------------------------------------------------------------------

# Sort and iterate, if current is same as last, skip, else add to result


def get_unique_elements(arr):
    unique = [''] * len(arr)
    i = 0

    for num in arr:
        if num not in unique:
            unique[i] = num
            i += 1

    return unique[:i]


print(get_unique_elements([10, 6, 7, 4, 6, 8, 9, 7, 11, 10]))
