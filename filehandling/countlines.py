count=0
with open('filehandling/hello.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        count+=1
print(count)
