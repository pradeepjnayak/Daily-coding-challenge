'''
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
''


from operator import mul
from functools import reduce


def sub_product_array(arr):
    if not isinstance(arr, list) or not arr:
        return []
    elem_product = reduce(mul, arr)
    new_arr = [elem_product//elem for elem in arr]
    return new_arr

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print("new array : {}".format(sub_product_array(arr)))
