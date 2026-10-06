with open('filehandling/hello.txt','w') as f:
    f.write('Hello world!')
    f.truncate(5)
with open('filehandling/hello.txt','r') as f:
    print(f.read())