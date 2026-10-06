# Create a shopping cart using a list. Write a program to:
# pythoncart = ["Laptop", "Mouse", "Keyboard"]
# Add "Monitor" to the cart
# Remove "Mouse" from the cart
# Check if "Laptop" is in the cart
# Display total items in cart
cart=['Lipgloss','Heels','Tanktop','Nails','Phonecover']
cart.append('Monitor😏')
cart.remove('Phonecover')
if 'Heels' in cart:
    print('Yes,ofcourse')
else:
    print('no')
print(cart)
print(len(cart))