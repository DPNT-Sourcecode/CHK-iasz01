
from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # check any illegal imput
        if not isinstance(skus, str):
            return -1
        for char in skus:
            if char not in 'ABCD':
                return -1
            
        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        offers = {'A': (3, 130), 'B': (2, 45)}

        counts = Counter(skus)
        total = 0

        for item, price in prices.items():
            count = counts.get(item, 0)
            if item in offers:
                qty, offer_price = offers[item]
                total += (count // qty)*offer_price+(count % qty) * price
            else:
                total += count * price
        return total

