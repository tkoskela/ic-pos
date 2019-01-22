

from icpos import checkout

itemsList = list()
pricesList = list()
referencePricesList = list()

# single item tests
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['A'])
referencePricesList.append(25)

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

# Remainder after offer tests
pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['B','A','A','A','A'])
referencePricesList.append(115)

pricesList.append({'A':25, 'B':40, 'P': 30})
itemsList.append(['B','B','B','B','P'])
referencePricesList.append(170)

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


for prices,items,ref in zip(pricesList,itemsList,referencePricesList):
    p = checkout(items, prices)
    if(p == ref):
        print('Test passed')
    else:
        print('Test failed')
        print(prices)
        print(items)
        print(ref)
        
