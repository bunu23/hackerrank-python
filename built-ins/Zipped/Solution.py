# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().splitlines()


    n, x = map(int, data[0].split())

    sheet = []

   
    for i in range(1, x + 1):
        sheet.append(list(map(float, data[i].split())))

    for i in zip(*sheet):
        print(f"{sum(i) / len(i):.1f}")
