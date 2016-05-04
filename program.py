import csv
import os
import statistics

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

# def get_price(p):
#     return p.price

def announce(item, msg):
    print('Pulling item {} for {}'.format(item, msg))
    return item


def query_data(data):
    data.sort(key=lambda p: p.price) #why not just use the attribute directly

    high_purchase = data[-1]
    print('the highest price is ${:,}'.format(int(high_purchase.price)))

    low_purchase = data[0]
    print('the lowest price is ${:,}'.format(int(low_purchase.price)))

    # average price of house?
    prices = [
        p.price
        for p in data
    ]
    avg_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(avg_price)))


    two_bed_homes = (
        p
        for p in data
        if announce(p, '2-bedrooms, found {}'. format(p.beds)) and p.beds == 2
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))
    print('Average 2-bedroom home is ${:,}, baths={}, sq ft={:,}'
          .format(int(avg_price), round(avg_baths,1), round(avg_sqft, 1)))


def main():
    print_header()
    filename = get_data_file()
    # print(filename)
    # print(os.path.isfile(filename))
    data = load_file(filename)
    query_data(data)




if __name__ == '__main__':
    main()