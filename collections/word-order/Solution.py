# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_word_occurrences():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    words = data[1:n+1]
    
    word_count = {}
    order_of_appearance = []
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            order_of_appearance.append(word)
    

    distinct_count = len(order_of_appearance)
    print(distinct_count)
    
  
    occurrences = [word_count[word] for word in order_of_appearance]
    print(' '.join(map(str, occurrences)))

count_word_occurrences()
