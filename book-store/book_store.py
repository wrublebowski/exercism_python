'''
One copy costs $8.
2 different books - you get 5% discount on those two books.
3 different books, you get a 10% discount.
4 different books, you get a 20% discount.
5, you get a 25% discount.

Note: that if you buy four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set,
but the fourth book still costs $8.

Calculate the price of any conceivable shopping basket (containing only books of the same series),
giving as big a discount as possible.
'''

from collections import Counter

basket = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]

def total(basket):


    regular_cost = 800
    discounts = {1:0.0, 2:0.05, 3:0.1, 4:0.2, 5:0.25}
    counts = Counter(basket)
    all_packets = []
    x = True
    while x == True:
        if basket == []:
            bill = 0
            break
        else:
            # keep gathering books into packets until basket is empty
            packet = [i for i in counts if counts[i] != 0]
            all_packets.append(len(packet))
            counts.subtract(packet)
            in_basket = sum(counts.values())
            if in_basket == 0:
                x = False
                print('pakiety do discountu:',all_packets)

# split 5 and 3 packets into 4 and 4 packets:

        while 3 in all_packets and 5 in all_packets:
            all_packets.remove(3)
            all_packets.remove(5)
            all_packets += [4,4]
            break
    print(all_packets)

    bill = 0
    for packet in all_packets:
        bill += ((packet * 800) - (packet*800)*discounts[packet])

    print(bill)
    return bill

total(basket)
