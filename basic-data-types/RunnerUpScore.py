if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Sort the list of scores in descending order
    sorted_scores = sorted(arr, reverse=True)
    
    # Find the runner-up score
    runner_up_score = None
    for score in sorted_scores:
        if score < max(sorted_scores):
            runner_up_score = score
            break
    
    print(runner_up_score)
