from collections import OrderedDict as ordered_dict
def main():
    items = ordered_dict()
    while True:
        try:
            item = input("").upper()
            if item:
                items = append_items(item, items)
        except EOFError:
            for item, amount in sorted(items.items()):
                print(f"{amount} {item}")
            return


def append_items(item, items):
    if item in items:
        items[item] += 1
        return(items)
    else:
        items[item] = 1
        return(items)

if __name__ == "__main__":
    main()