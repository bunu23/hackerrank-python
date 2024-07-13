if __name__ == '__main__':
    s = input().strip()
    

    from collections import Counter
    counts = Counter(s)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for i in range(3):
        char, count = sorted_counts[i]
        print(f"{char} {count}")
