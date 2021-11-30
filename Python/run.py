UNIT_PRICE = 87.00
units = 0
PurchasePrice =0.0
TotalPurchase =0.0

units = int(input("Please enter the number of units. "))

PurchasePrice = UNIT_PRICE*units

if units >= 500:
    TotalPurchase = PurchasePrice * 0.07
    print("You get a 7% discount. Your total purchase is " + \
          format(TotalPurchase, '.2f') + " dollars.")
    
elif units < 500 and units >= 100:
    TotalPurchase = PurchasePrice * 0.05
    print("You get a 5% discount. Your total purchase is " + \
          format(TotalPurchase, '.2f') + " dollars.")
else:
    TotalPurchase = PurchasePrice
    print("You get no discount. Your total purchase is " + \
          format(TotalPurchase, '.2f') + " dollars.")

