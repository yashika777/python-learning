# Restaurant Menu & Orders (All Data Structures)
# Restaurant management system:
# python# Menu (Dictionary)
# menu = {
#     "Pizza": 250,
#     "Burger": 120,
#     "Pasta": 180,
#     "Coffee": 50
# }
# # Daily specials (Tuple - unchangeable)
# specials = ("Monday Special", "Tuesday Discount", "Weekend Combo")
# # Current orders (List)
# orders = []
# # Unique customers today (Set)
# customers = set()
# Features to implement:
# 1. Display menu with prices
# 2. Take order (add to orders list)
# 3. Track customer ID (add to customers set)
# 4. Calculate bill for an order
# 5. Display today's special
# 6. Find most ordered item
# 7. Total revenue calculation
menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Coffee": 50,
    "Pav-Bhaji":100,
    "Veg-Thali":250
}
specials = ("Monday Special", "Tuesday Discount", "Weekend Combo")
orders = []
customers = set()
def frequency():
        fre={}
        for i in orders :
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        return fre

while True:
    print('''
---------Features----------
1).Display menu with price
2).Take customer id
3).Take order
4).Calculate bill for an order
5).Display Today's Special
6).Find most ordered item
7).Total revenue calculation
8).Exit
          ''')
    enter=int(input('Enter what you want sir/mam:'))
    if enter==1:
        for key,(item,value) in enumerate(menu.items(),start=1):
            print(key,item,':',value)
    elif enter==2:
        id=int(input('Enter customers id:'))
        current_customer=id
        customers.add(current_customer)
    elif enter==3:
        customer_order=[]
        order=input('Enter your order:')
        order=order.split(',')
        for item in order:
            item=item.strip()
            if item in menu:
                orders.append(item)
                customer_order.append(item)
            else:
                print('item not available')
    elif enter==4:
        bill=0
        for i in customer_order:
            b=menu[i]
            bill+=b
        print(current_customer,'Sir your total bis is'':',bill)
    elif enter==5:
        day=input('Enter day:')
        if day=='Monday':
            print("today's special",specials[0])
        elif day=='Tuesday':
            print("today's special",specials[1])
        elif day=='Saturday' or day=='Sunday':
            print("today's special",specials[2])
        else:
            print('Sorry we do not have any special offer today')
    elif enter==6:
        fre=frequency()
        highest=0
        for key,value in fre.items():
            if value>highest:
                highest=value
                item=key
        print('total orders:',len(orders))
        print('Most demanding item',item,':',highest)
    elif enter==7:
        revenue=0
        fre=frequency()
        for key,value in fre.items():
            revenue+=menu[key]*value
        print('Total revenue:',revenue)
    elif enter==8:
        print('Exiting....please visit again bye bye')
        break
    else:
        print('Invalid!!')
