def checkout(itemCodes, prices):

    """
    takes a list of item codes and their current prices and
    returns the total price in pence, after applying any relevant offers.
    """
    
    offerAmount = {'A': 3, 'B': 3}
    offerPrice = {'A': 2 * prices['A'], 'B': 100}

    price = 0

    for code in set(itemCodes):

        amount = itemCodes.count(code)
        
        if code in offerAmount.keys() and amount >= offerAmount[code]:

                price += offerPrice[code] * int(amount / offerAmount[code])
                price += amount % offerAmount[code] * prices[code]

        else:

            price += amount * prices[code]

    return price
