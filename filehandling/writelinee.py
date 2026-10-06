# line=['line1\n','line2\n','line3\n']
# with open('filehandling/hello.txt','w') as f:
#     f.writelines(line)
line=['line11','line22','line33']
with open('filehandling/hello.txt','w') as f:
    for L in line:
        f.write(L +'\n')