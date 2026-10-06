word='Hello'
i=1
with open('filehandling/copy.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        if word in line:
            print(i)
        i+=1
