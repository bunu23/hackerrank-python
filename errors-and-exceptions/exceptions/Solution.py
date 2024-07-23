# Enter your code here. Read input from STDIN. Print output to STDOUT
def handle_exceptions():
    import sys
    
   
    num_cases = int(input().strip())
    
    for _ in range(num_cases):
        try:
            a, b = input().strip().split()
            result = int(a) // int(b)  # Use // for integer division in Python 3
            print(result)
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")


handle_exceptions()
