from icpos import checkout, Checkout

itemsList = list()
pricesList = list()
referencePricesList = list()

# single item tests. First in list
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['A'])
referencePricesList.append(25)

# single item tests. Last in list
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['P'])
referencePricesList.append(30)

# multiple item test
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['A','B','P'])
referencePricesList.append(95)

# 3 for 100 offer test
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['B','A','B','P','B'])
referencePricesList.append(155)

# 3 for price of 2 tests
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['B','A','A','P','A'])
referencePricesList.append(120)

# same with different price
pricesList.append({'A':33, 'B':40, 'P': 30})
itemsList.append(['B','A','A','P','A'])
referencePricesList.append(136)

# Remainder after offer tests. 4 of the same.
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['B','A','A','A','A'])
referencePricesList.append(115)

# Remainder after offer tests. 5 of the same.
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['B','B','B','B', 'P', 'B'])
referencePricesList.append(210)

# 0 price tests
pricesList.append({'A':0, 'B':0, 'P': 0})
itemsList.append(['B','A','B','A','P'])
referencePricesList.append(0)

pricesList.append({'A':0, 'B':0, 'P': 0})
itemsList.append(['A','P','P','A'])
referencePricesList.append(0)

pricesList.append({'A':0, 'B':0, 'P': 0})
itemsList.append(['B','B','B','A','P'])
referencePricesList.append(100)

# Run tests using checkout function
for prices,items,ref in zip(pricesList,itemsList,referencePricesList):
    p = checkout(items, prices)
    
    if(p == ref):
        print('Test checkout passed')
    else:
        print('Test checkout failed')
        print(prices)
        print(items)
        print(ref)

# Run tests using Checkout object
for prices,items,ref in zip(pricesList,itemsList,referencePricesList):    
    c = Checkout(prices)
    for i in items:
        c.scan(i)

    if(c.total() == ref):
        print('Test Checkout passed')
    else:
        print('Test Checkout failed')
        print(prices)
        print(items)
        print(ref)
