# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def find_captains_room(k, room_list):
    room_counter = Counter(room_list)
    
    # Find the room number that appears only once
    for room, count in room_counter.items():
        if count == 1:
            return room

# Example usage
k = int(input().strip())
room_list = input().strip().split()
print(find_captains_room(k, room_list))
