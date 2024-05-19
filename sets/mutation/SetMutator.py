# Enter your code here. Read input from STDIN. Print output to STDOUT
# Reading input
n = int(input())
A = set(map(int, input().split()))
num_operations = int(input())

# Perform each operation
for _ in range(num_operations):
    operation_info = input().split()
    operation = operation_info[0]
    other_set_length = int(operation_info[1])
    other_set = set(map(int, input().split()))
    
    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

# Output the sum of elements in set A
print(sum(A))
