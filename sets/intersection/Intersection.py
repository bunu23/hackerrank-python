# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    # Input number of students subscribed to English newspaper and their roll numbers
    n_english = int(input())
    english_subscribers = set(map(int, input().split()))

    # Input number of students subscribed to French newspaper and their roll numbers
    n_french = int(input())
    french_subscribers = set(map(int, input().split()))

    # Find intersection of sets to get students subscribed to both newspapers
    total_subscribers = len(english_subscribers.intersection(french_subscribers))

    # Output the total number of students subscribed to both newspapers
    print(total_subscribers)

if __name__ == "__main__":
    main()
