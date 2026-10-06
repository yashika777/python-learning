# To-Do List Manager (List)
# Create a to-do list application:
#  To-do list structure
# tasks = []
# # Features to implement:
# 1. Add task
# 2. View all tasks
# 3. Mark task as complete (remove from list)
# 4. Count pending tasks
# 5. Clear all tasks
tasks=['Buy Groceries','Do homework','Wash Clothes','Go to College']
while True:
    print("""
----------To-Do List-----------
Features:
1) Add tasks
2) View all tasks
3)Mark task as completed
4)Count pending task
5)Clear all tasks
6) Exit 
          """)
    Enter=int(input('Enter your choice:'))
    if Enter==1:
        Newtask=input('Add new task:')
        tasks.append(Newtask)
    elif Enter==2:
        for number,task in enumerate(tasks,start=1):
            print(number,task)
    elif Enter==3:
        Completed_task=input('completed task:')
        if Completed_task in tasks:
            tasks.remove(Completed_task)
        else:
            print("no such task exist!!")
    elif Enter==4:
        print('Pending Task:',len(tasks))
    elif Enter==5:
        while tasks:
            tasks.pop()
        print('All task cleared')
    elif Enter==6:
        print("""Exiting......
              bye 👋 """)
        break
    else:
        print('Invalid')
    
    
