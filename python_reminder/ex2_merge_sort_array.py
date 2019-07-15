# --------------------------------------------------------------------------
# EXERCISE 2: Write an O(n) Python function that merges two sorted arrays
# so that the resultant array is also sorted.
#
# For example, if A=[3,6,10,15] and B=[7,10,12,19,25],
# the resulting combined array would be [3,6,7,10,10,12,15,19,25]
# --------------------------------------------------------------------------


def merge_sort_array(a, b):
    i_a = 0
    i_b = 0
    combined = [0] * (len(a) + len(b))

    for i in range(len(a) + len(b)):
        # If all values of a have been added
        if i_a == len(a):
            combined[i] = b[i_b]
            i_b += 1
            continue

        # If all values of b have been added
        if i_b == len(b):
            combined[i] = a[i_a]
            i_a += 1
            continue

        # Append to combined array smaller value between a and b at current index
        if a[i_a] <= b[i_b]:
            combined[i] = a[i_a]
            i_a += 1
        else:
            combined[i] = b[i_b]
            i_b += 1

    return combined


a = [3, 6, 10, 15]
b = [7, 10, 12, 19, 25]
print(merge_sort_array(a, b))
