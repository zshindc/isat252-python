#Total Purchase Program
#Programmer: Zachary Shin
#Language: Python 3.9.x
#total_purchase.py

#declare price of 5 store items
item1=0.0
item2=0.0
item3=0.0
item4=0.0
item5=0.0

#get price of items (input)
item1=float(input('Enter price of first item: '))
item2=float(input('Enter price of second item: '))
item3=float(input('Enter price of third item: '))
item4=float(input('Enter price of fourth item: '))
item5=float(input('Enter price of fifth item: '))

#calculate subtotal of the sale, sales tax, and total (processing)
subtotal_sale=item1+item2+item3+item4+item5
sales_tax=subtotal_sale*0.06
total=subtotal_sale+sales_tax

#display subtotal, sales tax, and total (output)
print('The subtotal of the sale is', format(subtotal_sale,'.2f'), 'dollars.') 
print('The sales tax is', format(sales_tax,'.2f'), 'dollars.')
print('The total is', format(total,'.2f'), 'dollars.')
