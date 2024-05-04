def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        substring = string[i:i+k]
        distinct_chars = []
        for char in substring:
            if char not in distinct_chars:
                distinct_chars.append(char)
        print(''.join(distinct_chars))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
