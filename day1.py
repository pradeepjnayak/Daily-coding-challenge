'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''



def sum_exists(arr, sum):
    for elem in arr:
        if (sum-elem) in arr:
            return True
    return False

if __name__ == '__main__':
    arr = [10, 15, 3, 8]
    k = 17

    print(" Does list add up ? ={}".format(sum_exists(arr,k)))
