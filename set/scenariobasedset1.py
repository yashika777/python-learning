# A theater has seats numbered 1 to 10. Create a set of booked seats:
# pythonbooked_seats = {2, 5, 7, 9}
# Write a program to:
# Book seat number 3
# Check if seat 5 is available
# Find all available seats (1-10)
# Cancel booking for seat 7
booked_seats={2,3,6,5,7,9}
booked_seats.add(3)
if 5 not in booked_seats:
    print('Available')
booked_seats.remove(7)
available_seat=[]
for i in range(1,11):
    if i not in booked_seats:
        available_seat.append(i)
print(booked_seats)
print(available_seat)