def checkout(itemCodes, prices):

    """
    takes a list of item codes and their current prices and
    returns the total price in pence, after applying any relevant offers.
    """
    
    offerAmount = {'A': 3, 'B': 3}
    offerPrice = {'A': 2 * prices['A'], 'B': 100}

    price = 0

    for code in set(itemCodes):

        if code in prices.keys():
        
            amount = itemCodes.count(code)
        
            if code in offerAmount.keys() and amount >= offerAmount[code]:

                price += offerPrice[code] * int(amount / offerAmount[code])
                price += amount % offerAmount[code] * prices[code]
                
            else:
                
                price += amount * prices[code]

        else:

            print('Error: Unknown item code ' + code)

    return price


class Checkout():

    """
    Can be instantiated with the current prices. Provides two methods: scan(itemCode) and total()
    The latter should be callable at any time to obtain a correct total for the items scanned so far.
    """
    
    def __init__(self, prices):

        setattr(self,'prices',prices)
        setattr(self,'items',list())

    def scan(self,itemCode):

        if(itemCode in self.prices.keys()):
            self.items.append(itemCode)
        else:
            print('Error: Unknown item code ' + itemCode)

    def total(self):

        return checkout(self.items, self.prices)

    def printItems(self):

        print(self.items)

    def printPrices(self):
        
        print(self.prices)
