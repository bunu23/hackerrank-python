if __name__ == "__main__":
    n = int(input()) 
    integer_list = map(int, input().split())  
    

    tuple_of_integers = tuple(integer_list)
    
 
    result = hash(tuple_of_integers)

    print(result)
