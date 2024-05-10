# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_distinct_stamps(num_stamps, stamps):
    distinct_stamps = set()
    for stamp in stamps:
        distinct_stamps.add(stamp)
    return len(distinct_stamps)

if __name__ == "__main__":
    num_stamps = int(input())
    stamps = [input().strip() for _ in range(num_stamps)]
    result = count_distinct_stamps(num_stamps, stamps)
    print(result)
