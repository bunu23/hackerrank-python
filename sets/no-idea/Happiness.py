# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_happiness(n, m, arr, A, B):
    happiness = 0
    
    set_A = set(A)
    set_B = set(B)
    
    for num in arr:
        if num in set_A:
            happiness += 1
        elif num in set_B:
            happiness -= 1
    
    return happiness

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = calculate_happiness(n, m, arr, A, B)
    print(result)
