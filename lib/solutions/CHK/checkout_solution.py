
from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # check any illegal imput
        if not isinstance(skus, str):
            return -1
        for char in skus:
            if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return -1
            
        prices = {
            'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
            'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
            'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
            'S': 20 ,'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
            'Y': 20, 'Z': 21
            }
        
        offers = {
            'A': [(5, 200), (3, 130)],
            'B': [(2, 45)],
            'H': [(10, 80), (5, 45)],
            'K': [(2, 120)],
            'P': [(5, 200)],
            'Q': [(3, 80)],
            'V': [(3, 130), (2, 90)]
            }
        
        counts = Counter(skus)

        # These are the cross items
        free_b = min(counts.get('B', 0), counts.get('E', 0) // 2)
        free_q = min(counts.get('Q', 0), counts.get('R', 0) // 3)
        free_m = min(counts.get('M', 0), counts.get('N', 0) // 3)
        # Same items free offer
        free_f = counts.get('F', 0)//3
        free_u = counts.get('U', 0)//4

        #Dict for frree items to stop if repeating loop
        free_counts = {
            'B': free_b,
            'F': free_f,
            'M': free_m,
            'Q': free_q,
            'U': free_u
        }
        # Group items
        total = 0

        group_items = ['S', 'T', 'X', 'Y', 'Z']
        price_list = []
        for item in group_items:
            price_list.extend([prices[item]] * counts.get(item, 0))
        if price_list:
            price_list.sort(reverse=True)
            num_groups = len(price_list) // 3
            group_total = num_groups * 45
            remainder_total = sum(price_list[-(len(price_list) % 3):]) if len(price_list) % 3 > 0 else 0
            total += group_total + remainder_total
            for item in group_items:
                counts[item] = 0

        for item, price in prices.items():
            count = counts.get(item, 0)
            count -= free_counts.get(item, 0)
            if count < 0:
                count = 0
        
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

