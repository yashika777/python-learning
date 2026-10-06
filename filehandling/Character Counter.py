vowels=0
constants=0
characters=0
with open('filehandling/hello.txt','w') as f:
     f.write('Hello  Write  a program  123  to count total words in a text file.\nhii 2hello')
with open('filehandling/hello.txt') as f:
    for i in f.read():
        if i in ['A','E','I','O','U','a','e','i','o','u']:
            vowels+=1
        elif not i.isspace() and not i.isdigit():
            constants+=1
    characters=constants+vowels
print(f"""Characters= {characters}
Vowels={vowels}
Constants={constants}""")

        
