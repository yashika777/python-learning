#  Create a dictionary to store student names as keys and their marks as values:
# pythonstudents = {"Raj": 85, "Priya": 92, "Amit": 78}
# Write a program to:
# Find the student with highest marks
# Add a new student "Sneha" with marks 88
# Update Raj's marks to 90
# Calculate average marks of all students
d={'Rajpal':90,"Priya":87,"Varsha":95,"Amit":78}
sum=0
highest=0
for Key,value in d.items():
    if highest<value:
        highest=value
    sum+=value
    avg=sum/len(d)
print(highest)
print(avg)
d['Sneha']=88
d['Rajpal']=92
print(d)


