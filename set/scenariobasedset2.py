# Store employee IDs in a set (to ensure uniqueness):
# pythonemployees = {101, 102, 103, 104}
# Write a program to:
# Add new employee ID 105
# Try adding duplicate ID 102 and observe
# Remove employee ID 103
# Find total employees
pythonemployees = {101, 102, 103, 104}
pythonemployees.update([105,102])
print(pythonemployees)
pythonemployees.remove(105)
print(pythonemployees)
print(len(pythonemployees))
