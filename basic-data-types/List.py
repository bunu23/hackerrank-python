if __name__ == '__main__':
    N = int(input())
    commands = []
    
    for _ in range(N):
        commands.append(input().split())
        
    # Initialize empty list
    my_list = []
    
    for command in commands:
        if command[0] == "insert":
            # insert i e: Insert integer e at position i
            i = int(command[1])
            e = int(command[2])
            my_list.insert(i, e)
        elif command[0] == "print":
            # print: Print the list
            print(my_list)
        elif command[0] == "remove":
            # remove e: Delete the first occurrence of integer e
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == "append":
            # append e: Insert integer e at the end of the list
            e = int(command[1])
            my_list.append(e)
        elif command[0] == "sort":
            # sort: Sort the list
            my_list.sort()
        elif command[0] == "pop":
            # pop: Pop the last element from the list
            my_list.pop()
        elif command[0] == "reverse":
            # reverse: Reverse the list
            my_list.reverse()
