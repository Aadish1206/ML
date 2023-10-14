def compress(chars):
    nextchar = 0  #We read and write the nextchar pointer
    read = 0   # Read pointer
    n = len(chars)

    while read < n:
        current_char = chars[read]
        count = 0

        while read < n and chars[read] == current_char:
            read += 1
            count += 1
            #print(current_char)
          
        chars[nextchar] = current_char
        nextchar += 1
        #print(nextchar)
      
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[nextchar] = digit
                nextchar += 1
                
    
    chars = chars[:nextchar]

    return len(chars)

# Example usage:
chars = ["a", "a", "b", "b", "c", "c", "c"]
result_len = compress(chars)
print(chars)       
print(result_len)  
