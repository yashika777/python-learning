num = (45, 23, 67, 12, 89, 34)
minimum=0
maximum=0
for i in num:
    if i>maximum:
        maximum=i
        minimum=maximum
for j in num:
    if i<minimum :
        minimum=i
print(f'Maximum={maximum}')
print(f'Minimum={minimum}')