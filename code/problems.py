"""Bubble Sort: Q65"""
# sorting algorithm that works by repeatedly swapping the adjacent
# elements if they are in wrong order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

"""Star Triangle: Q66"""
def star(h):
    for i in range(h):
        print(" "*(h-i-1)+"*"*(2*i+1))

"""Produce Fibonacci Numbers: Q67"""
def generate_fib(n):
    """Finonacci is a series of numbers in which each number is the sum of the two preceding numbers"""
    # 1,1,2,3,5,8,13,21 ...
    if n == 0:
        return 
    elif n == 1:
        return [1]
    else:
        result = [1,1]
        for i in range(n-2):
            result.append(result[i]+result[i+1])
        return result

def is_prime(num):
    """A number is prime if it is only divisible by 1 and itself: Q68"""
    # 2,3,5,7,11,13,17,19,23,29,31,37,41 ...
    if num < 2:
        return False
    else:
        for n in range(num-1,1,-1):
            if num % n == 0:
                return False
        return True
    
def is_palindrome(s):
    """A palindrome is a string that is the same read forward or backward: Q69"""
    # 'mom' , 'civic', 'reviver'
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

def non_recursive_palindrome(s):
    return s == s[::-1]

def roman_to_int(numeral):
    """Use subtractive notation to avoid 4 characters being repeated in succession. 
    I before V or X, 
    X before L or C,
    C before D or M

    Iterate through each roman numeral char and maintain the sum. Q70
    """
    conversion_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i, size = 0, len(numeral)
    result = 0
    while i < size-1:
        if numeral[i] == "I":
            if numeral[i+1] == "V" or numeral[i+1] == "X":
                result += conversion_map[numeral[i+1]] - 1
            else:
                result += conversion_map[numeral[i]]
        elif numeral[i] == "X":
            if numeral[i+1] == "L" or numeral[i+1] == "C":
                result += conversion_map[numeral[i+1]] - 1
            else:
                result += conversion_map[numeral[i]]
        elif numeral[i] == "C":
            if numeral[i+1] == "D" or numeral[i+1] == "M":
                result += conversion_map[numeral[i+1]] - 1
            else:
                result += conversion_map[numeral[i]]
        else:
            result += conversion_map[numeral[i]]
        i += 1
        if i == size-1:
            result += conversion_map[numeral[i]]

    return result

if __name__ == "__main__":
    import copy
    arr = [4,1,5,8,19,23,35,21,1039,4339,239,-1, 0,25,645] 
 
    s = copy.deepcopy(arr)
    # [1, 4, 5, 8]
    # []
    arr.sort()
    assert bubble_sort(s) == arr

    # star(9)
    # print('\n')
    # star(4)
    assert generate_fib(2) == [1,1]
    
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41]
    for i in range(len(primes)):
        assert is_prime(primes[i])
    
    assert is_palindrome('civic')
    assert not is_palindrome('mississippi')
    assert roman_to_int("XVII") == 17
    assert roman_to_int("MCV") == 1105
