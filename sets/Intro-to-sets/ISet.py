def average(array):
    # your code goes here
    distinct_heights = set(array)
    sum_of_heights = sum(distinct_heights)
    average_height = sum_of_heights / len(distinct_heights)
    return round(average_height, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
