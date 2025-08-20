
from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # check any illegal imput
        if not isinstance(skus, str):
            return -1
        for char in skus:
            if char not in 'ABCDEF':
                return -1
            
        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
        offers = {
            'A': [(5, 200), (3, 130)],
            'B': [(2, 45)]
            }
        
        counts = Counter(skus)

        #cross_offers = [
        #    {'source': 'E', 'req': 2, 'target': 'B', 'free': 1}
        #]
        free_b = min(counts.get('B',0), counts.get('E', 0) // 2)

        #new offer
        free_f = counts.get('F', 0)//3
        total = 0

        for item, price in prices.items():
            count = counts.get(item, 0)
            if item == 'B':
                count -= free_b
            if item =='F':
                count -= free_f
            if item in offers:
                sorted_offers = sorted(offers[item], key=lambda x: x[0], reverse=True)
                sub_count = count
                item_total = 0
                for qty, offer_price in sorted_offers:
                    item_total += (sub_count //  qty)*offer_price
                    sub_count %=qty
                item_total += sub_count*price
                total += item_total
            else:
                total += count * price
        return total


