print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************''')

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

menu = appetizers + entrees + desserts + drinks
customer_order = {}

print('''
Appetizers
----------''')
for appetizer in appetizers:
  print(appetizer)

print('''
Entrees
-------''')
for entree in entrees:
  print(entree)

print('''
Desserts
--------''')
for dessert in desserts:
  print(dessert)

print('''
Drinks
------''')
for drink in drinks:
  print(drink)

print('''
***********************************
** What would you like to order? **
***********************************''')

while True:
  order = input('> ')
  if order == 'quit':
    print(f'Thank you! Your final order is: {customer_order}')
    break
  elif order in menu:
    if order not in customer_order:
      customer_order[f'{order}'] = 0
      customer_order[order] += 1
      print(f'** {customer_order[order]} order of {order} has been added to your meal **')
    elif order in customer_order:
      customer_order[order] += 1
      print(f'** {customer_order[order]} orders of {order} have been added to your meal **')
  elif order not in menu:
    print('Sorry, no custom orders. Please see the menu above!')