def checkout(itemCodes, prices):

    """
    takes a list of item codes and their current prices and
    returns the total price in pence, after applying any relevant offers.
    """

    # Define offers
    offerAmount = {'A': 3, 'B': 3}
    offerPrice = {'A': 2 * prices['A'], 'B': 100}

    # Initialize price
    price = 0

    # Loop through a set of unique item codes
    for code in set(itemCodes):

        # Check if the item code has a price associated with it
        if code in prices.keys():

            # Count the number of occurrences of this code
            amount = itemCodes.count(code)

            # Check if the item code has an offer
            # Assuming only one offer per item
            if code in offerAmount.keys() and amount >= offerAmount[code]:

                # Add the offer price for each completed offer. Add the regular price for the remainder.
                price += offerPrice[code] * int(amount / offerAmount[code])
                price += amount % offerAmount[code] * prices[code]
                
            else:

                # Add the regular price for each item
                price += amount * prices[code]

        else:

            # Print an error if the item code does not have a price, add nothing to the total.
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
