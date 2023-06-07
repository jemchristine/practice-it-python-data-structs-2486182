from collections import namedtuple
from csv import reader

def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as csv_file:
    #Create workable objects with each line
        read = reader(csv_file)
        Customer = namedtuple("Customer", next(read))
        for row in read:
            customer = Customer(*row)
            print(customer.CustomerID, customer.FirstName,
                  customer.LastName, customer.Email)
    return

if __name__ == "__main__":
    main()