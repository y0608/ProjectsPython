f=open('words.txt','r')
string_without_line_breaks = ""
bestlen=0
words=0
for line in f:
    words+=1
    if(len(line)>bestlen):
        bestlen=len(line)
print(words)
f.close()