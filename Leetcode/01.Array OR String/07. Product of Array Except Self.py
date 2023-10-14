def product_array(array):
    n = len(array)
    current_list = [1] * n  
    #print(current_list)
    before_list = [1] * n
    #print(before_list)
    next_list = [1] * n
    #print(next_list)
    
    # Calculate pre-product array
    before_product = 1
    for i in range(n):
        before_list[i] = before_product
        #print(before_list)
        before_product *= arr[i]
        #print(before_product)

    # Calculate post-product array
    next_product = 1
    for i in range(n - 1, -1, -1):
        next_list[i] = next_product
        #print(next_list)
        next_product *= arr[i]
        #print(next_product)

    # Construct the product array
    for i in range(n):
        current_list[i] = before_list[i] * next_list[i]
        #print(current_list)

    return current_list

array = [0,2,3]
result = product_array(array)
print(result)
