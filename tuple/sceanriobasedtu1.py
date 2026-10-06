# Create a tuple of book categories (non-changeable):
# pythoncategories = ("Fiction", "Science", "History", "Technology")
# Write a program to:
# Check if "Science" exists
# Find the index of "History"
# Count total categories
tu=('Fiction','Science','History','Technology')
if 'Science' in tu:
    print('exist')
else:
    print('no')
print(len(tu))
print(tu.index('History'))