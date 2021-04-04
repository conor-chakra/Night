hot_day = True
cold_day = False
if hot_day:
    print('drink plenty of water and enjoy yourself')
    print('dont forget to wear sunscreen')
elif cold_day:
    print('It is a cold day so make sure to wear lots of layers')
else:
    print('It is a medium temperature day')

# e.g. a price of a house is 1m. If buyer has good credit they need to put down 10% otherwise they need to put down 20 %. print the down payment
price = 1000000
buyer_good_credit = True
if buyer_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'down_payment:£{down_payment}')
