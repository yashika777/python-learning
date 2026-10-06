with open('filehandling/copy.txt','w') as f:
    with open('filehandling/hello.txt','r') as j:
        for i in j:
            f.write(i)
