# create a product and price for three items
p1_name, p1_price = "Books", 49.99
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print(f"\t\t{company_name.title()}")
print(f"\t\t{company_address}")
print(f"\t\t{company_city}")

# print a line between sections
print("=" * 50)

# print out header for section of items
print("\tProduct Name \tProduct Price")

# create a print statement for each product
print(f"\t{p1_name.title()}\t\t${p1_price}")
print(f"\t{p2_name.title()}\t\t${p2_price}")
print(f"\t{p3_name.title()}\t\t${p3_price}")

# print a line between sections
print("=" * 50)

# print out header for sections of total
print("\t\t\tTotal")

# calculate total price and print out
total = p1_price + p2_price + p3_price
print(f"\t\t${total}")

# print a line between sections
print("=" * 50)

# output a thank you message
print(f"\n\t{message}\n")
