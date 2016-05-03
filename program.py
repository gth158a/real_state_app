import csv
import os

from data_types import Purchase


def print_header():
    print('---------------------------------')
    print('         REAL STATE APP')
    print('---------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):

    with open(filename, 'r', encoding= 'utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
            #print(type(row), row)

        #print(purchases[0].__dict__)

        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(type(row), row)

def get_price(p):
    return p.price

def query_data(data: list[Purchase]):
    data.soer(key=get_price)


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    # print(os.path.isfile(filename))
    data = load_file(filename)
    query_data(data)




if __name__ == '__main__':
    main()