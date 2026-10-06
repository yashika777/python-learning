# Create a dictionary to track book availability:
# pythonlibrary = {
#     "Python Basics": 5,
#     "Data Science": 3,
#     "Web Development": 0,
#     "AI Fundamentals": 7}
# Write a program to:
# Issue one copy of "Python Basics" (decrease count by 1)
# Check which books are out of stock (count = 0)
# Add a new book "Machine Learning" with 4 copies
pythonlibrary = {"Python Basics": 5,"Data Science": 3,"Web Development": 0,"AI Fundamentals": 7}
pythonlibrary['Python Basics']-=1
for key,value in pythonlibrary.items():
    if value==0:
        print("out of stock books:",key)
pythonlibrary['Ml']=4
print(pythonlibrary)
