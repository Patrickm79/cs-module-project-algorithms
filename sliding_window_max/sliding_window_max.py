'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):

#     window_array = [] # create window array
#     expected_output = [] # expected output

#     while 0 < len(nums) - (k-1): # loop (first pass is 1, so ind0, ind1, ind2. 2nd pass is 2, so ind1, ind2, ind3)

#         for number in nums[0:k]: # loop over numbers in window
#             window_array.append(number) #append numbers to window_array
#         window_array.sort() # sort window array
#         max_number = window_array[k-1] # get the last element of the window array
#         expected_output.append(max_number) # append max to expected_output
#         nums.pop(0) # delete first number of nums array, so next window starts
#         window_array = [] # clear the window_array to start fresh on next loop

#     return expected_output # return expected output

### Optimized Solution ###
def sliding_window_max(nums, k):
    expected_output = [] # create expected output
    while 0 < len(nums) - (k-1): # check that we are within the window space allowed and loop while true
        window_array = nums[0:k] # create the window
        expected_output.append(max(window_array)) # append the max of the window array to expected output
        nums.pop(0) # delete first number of nums array, so next window starts
    return expected_output # return expected output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
