inside_word=False
count=0
with open('filehandling/hello.txt','w') as f:
     f.write('Hello  Write  a program    to count total words in a text file.\nhii hello')
with open('filehandling/hello.txt','r') as f:
     for i in f.read():
        if not i.isspace() and not inside_word:
               count+=1
               inside_word=True
        elif i.isspace():
             inside_word=False
print(count)
               
        