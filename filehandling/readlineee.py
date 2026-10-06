with open('filehandling/hello.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        print(line,end='') #here print gives a new line automatically and readline too so we can see a blank line after every line so to avoid that end='' is used
