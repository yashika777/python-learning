#  Create a dictionary for product prices:
# pythonproducts = {"Laptop": 45000, "Mouse": 500, "Keyboard": 1500}
# Write a program to:
# Calculate total cart value
# Apply 10% discount if total > 40000
# Add a new product "Headphones" with price 2000
i={'Lipgloss':500,'Heels':600,'Bodycon':800,'Keyboard':1500}
total=0
for value in i.values():
    total+=value
if total>1000:
    discount=total*0.1
    total-=discount
i['Headphones']=2000
print(total)
print(i)



