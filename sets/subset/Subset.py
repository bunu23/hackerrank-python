# Enter your code here. Read input from STDIN. Print output to STDOUT

def check_subsets():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    test_cases = int(data[0].strip())
    index = 1
    
    results = []
    
    for _ in range(test_cases):
        # Number of elements in set A
        num_elements_A = int(data[index].strip())
        index += 1
        
        # Elements of set A
        set_A = set(data[index].strip().split())
        index += 1
        
        # Number of elements in set B
        num_elements_B = int(data[index].strip())
        index += 1
        
        # Elements of set B
        set_B = set(data[index].strip().split())
        index += 1
        
        # Check if set A is a subset of set B
        results.append(set_A.issubset(set_B))
    
    for result in results:
        print(result)

# Example usage:
if __name__ == "__main__":
    check_subsets()
