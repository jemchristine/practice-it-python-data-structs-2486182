from collections import namedtuple, defaultdict
from csv import reader
from pprint import pprint


def main():
    # add code here
    res = defaultdict(int)
    with open("data/OrderItems.csv", "r") as csv_file:
        read = reader(csv_file)
        Item = namedtuple("Item", next(read))
        for line in read:
            item = Item(*line)
            res[item.ProductID] += int(item.Quantity)
    pprint(dict(res))
    return


if __name__ == "__main__":
    main()
