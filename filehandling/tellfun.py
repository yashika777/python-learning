with open('filehandling/hello.txt','r') as f:
    print(f.read(8))
    position=f.tell()
    print(f.seek(position))
    print(f.read(3))