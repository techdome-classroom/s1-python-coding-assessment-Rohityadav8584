def matches(message: str, key: str) -> bool:
    m, k = len(message), len(key)
    i, j = 0, 0
    
    while i < m and j < k:
        if key[j] == '?':
            # Move both pointers when there's a '?'
            i += 1
            j += 1
        elif key[j] == '*':
            # '*' can match empty or any sequence of letters
            if j + 1 == k:  # If '*' is the last character in key
                return True
            j += 1  # Move key pointer to check next character after '*'
            while i < m and (j < k and message[i] != key[j]):
                i += 1  # Skip characters in message until a match is found
        else:
            if message[i] != key[j]:
                return False
            i += 1
            j += 1
    
    # If there are remaining characters in the key
    while j < k and key[j] == '*':
        j += 1
        
    return i == m and j == k

# Testing the function with example cases
print(matches("aa", "a"))    # False
print(matches("aa", "*"))    # True
print(matches("cb", "?a"))   # False
