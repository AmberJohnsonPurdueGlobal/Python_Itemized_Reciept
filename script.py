lovely_loveseat_name = "Lovely Loveseat "

lovely_loveseat_description = '''Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''

a_float = 254.00
lovely_loveseat_price = a_float

stylish_settee_name ="Stylish Settee "
stylish_settee_description = '''Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''

a_float = 180.50
stylish_settee_price = a_float

luxurious_lamp_name = "Luxurious Lamp "
luxurious_lamp_description = '''Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'''

a_float = 52.15
luxurious_lamp_price = a_float

a_float = .088
sales_tax = a_float

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_name

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_name

customer_one_tax = customer_one_total * sales_tax

print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)

