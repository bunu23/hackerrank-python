# Enter your code here. Read input from STDIN. Print output to STDOUT
def can_stack_cubes(test_cases):
    results = []
    
    for blocks in test_cases:
        left, right = 0, len(blocks) - 1
        last_cubed = float('inf')  

        while left <= right:
            if blocks[left] >= blocks[right]:
                current = blocks[left]
                left += 1
            else:
                current = blocks[right]
                right -= 1

            if current > last_cubed:
                results.append("No")
                break
            
            last_cubed = current
        else:
            results.append("Yes")

    return results


if __name__ == "__main__":
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        test_cases.append(blocks)

    results = can_stack_cubes(test_cases)
    
    for result in results:
        print(result)
