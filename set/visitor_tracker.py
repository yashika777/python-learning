# Unique Visitor Tracker (Set)
# Track unique website visitors:
# python# Visitor tracking
# visitors = set()
# Features to implement:
# 1. Add visitor (by user ID)
# 2. Count unique visitors
# 3. Check if user visited before
# 4. Find common visitors between two days
# 5. Find new visitors today
day1={101,202,123,145,267,203}
day2={245,143,200,102,203,105}
while True:
    print(""" 
---------------Visitor Tracking------------------
1). Add visitors by user id
2). Count Unique Visitors
3). Check if user visited before
4). Find common visitors between 2 days
5). Find new visitors today
6). Exit""")
    enter=int(input("Enter your choice:"))
    if enter==1:
        New_visitor=int(input('Enter id:'))
        day=int(input('Enter day 1 or 2:'))
        if day==1:
            day1.add(New_visitor)
        elif day==2:
            day2.add(New_visitor)
        else:
            print('Invalid!!')
    elif enter==2:
        print('Day 1 visitor',len(day1))
        print('Day 2 visitor',len(day2))
    elif enter==3:
        User=int(input('Enter id:'))
        if User in day1 and User in day2:
            print('This user has visted on both days') 
        elif User in day1:
            print("This user has visited on day1")
        elif User in day2:
            print('This user has visited on day2')
        else:
            print('This user have not visited before')
    elif enter==4:
        Common_visitor=day1&day2
        print('Common visitors on both days were:',Common_visitor)
    elif enter==5:
        new__visitors=day2-day1
        print('New visitors are:',new__visitors)
    elif enter==6:
        print('Exiting.....bye bye😘')
        break
    else:
        print('invalid !! ')
