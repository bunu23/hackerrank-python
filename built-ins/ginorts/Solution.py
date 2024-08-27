# Enter your code here. Read input from STDIN. Print output to STDOUT
def custom_sort(s):

    lowercase = [ch for ch in s if ch.islower()]
    uppercase = [ch for ch in s if ch.isupper()]
    odd_digits = [ch for ch in s if ch.isdigit() and int(ch) % 2 != 0]
    even_digits = [ch for ch in s if ch.isdigit() and int(ch) % 2 == 0]
    

    lowercase.sort()
    uppercase.sort()
    odd_digits.sort()
    even_digits.sort()
    
    
    result = ''.join(lowercase + uppercase + odd_digits + even_digits)
    
    return result


if __name__ == '__main__':
    import sys
    input = sys.stdin.read().strip()
    print(custom_sort(input))
