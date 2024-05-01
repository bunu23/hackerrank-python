def print_rangoli(size):
    # your code goes here
    import string
    alphabets = string.ascii_lowercase
    width = 4 * size - 3
    for i in range(size - 1, 0, -1):
        row = '-'.join(alphabets[size - 1:i:-1] + alphabets[i:size])
        print(row.center(width, '-'))
    center_row = '-'.join(alphabets[size - 1::-1] + alphabets[1:size])
    print(center_row.center(width, '-'))
    for i in range(1, size):
        row = '-'.join(alphabets[size - 1:i:-1] + alphabets[i:size])
        print(row.center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
