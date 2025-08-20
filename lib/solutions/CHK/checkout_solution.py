
from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # check any illegal imput
        if not isinstance(skus, str):
            return -1
        for char in skus:
            if char not in 'ABCDE':
                return -1
            
        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
        offers = {
            'A': [(3, 130), (5, 200)],
            'B': (2, 45)
            }
        cross_offers = {
            {'source': 'E', 'req': 2, 'target': 'B', 'free': 1}
        }

        counts = Counter(skus)

        # Handle cross item to calc free adjustments 
        free_adjust = {}
        for offer in cross_offers:
            source_count = counts.get(offer['source'], 0)
            target_count = counts.get(offer['target'], 0)
            if source_count > 0 and target_count > 0:
                num_apps = min(source_count // offer['req'], target_count // offer['free'])
                free_adjust[offer['target']] = free_adjust.get(offer['target'], 0) + num_apps * offer['free']


        total = 0

        for item, price in prices.items():
            count = counts.get(item, 0)
            # free adjustments cross offer stuff
            payable = count - free_adjust.get(item, 0)
            if payable < 0:
                payable = 0 # prevents min


            if item in offers and offer[item]:
                item_offers = sorted(offers[item], key=lambda x: x[0], reverse=True)
                rem = payable
                for qty, offer_price in item_offers:
                    num = rem // qty
                    total += num * offer_price
                    rem %= qty
                total += rem * price
            else:
                total += payable * price
        return total

