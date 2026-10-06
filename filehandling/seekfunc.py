with open('filehandling/hello.txt','r') as f:
    f.seek(10)
    print(f.read(5))
