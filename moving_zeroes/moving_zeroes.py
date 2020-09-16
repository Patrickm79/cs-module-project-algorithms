'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    i = 0
    j = len(arr) - 1

    while i < j:
        # Check for zero at i
        if arr[i] == 0:
            # while i is less than j
            # If j isn't zero, swap, move pointers, and break
            # Otherwise, move j down
            while i < j:
                if arr[j] != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                    break
                else:
                    j -= 1
        else:
            # if not 0, increment i
            i += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")