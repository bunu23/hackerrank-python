# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())


polynomial = input()


result = eval(polynomial)


print(result == k)
