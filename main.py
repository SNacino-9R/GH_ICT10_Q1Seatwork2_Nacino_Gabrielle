from pyscript import display


restaurant_name = 'Aromata' #string
owner_name = 'Jimmy Bondoc & Esper Dela Cruz' #string
year_established = "Since 2023" #string
popular_item_price = "P599 Meat Platter" #string
has_delivery = False #boolean
product_names = "Angus Steak, Crispy Chicken Wings, Creme Brulee" #list
business_hours = '11 AM - 1 AM' #string
menu_prices = (499, 399, 299) #dictionary

display(f'Owned by: {owner_name}')
display(year_established)
display(f'Opens: {business_hours}')
display(f'Menu:{product_names}')
display(f'Popular Item: {popular_item_price}')

