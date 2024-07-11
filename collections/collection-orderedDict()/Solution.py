# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict


def calculate_net_prices(num_items, items):
    ordered_dict = OrderedDict()
    
    for item in items:
        item_name, item_price = item.rsplit(' ', 1)
        item_price = int(item_price)
        
        if item_name in ordered_dict:
            ordered_dict[item_name] += item_price
        else:
            ordered_dict[item_name] = item_price
    
    for item_name, net_price in ordered_dict.items():
        print(f"{item_name} {net_price}")


if __name__ == "__main__":
    num_items = int(input().strip())
    items = [input().strip() for _ in range(num_items)]
    calculate_net_prices(num_items, items)
