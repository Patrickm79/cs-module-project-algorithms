'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    product = 1
    zeroes = 0

    for num in arr:
        if num == 0:
            zeroes += 1
            if zeroes > 1: # if there are more than one zero
                return [0] * len(arr) # all of the products are going to be 0
        else:
            product *= num

    result = []

    # If there is one zero what we append depends on whether the current number is 0
    if zeroes == 1:
        for num in arr:
            result.append(0) if num != 0 else result.append(product)
    # Otherwise, we just append the total product divided by the current number
    else:
        for num in arr:
            result.append(product // num)

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
