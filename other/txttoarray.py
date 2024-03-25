f=open('words.txt','r+')
string_without_line_breaks = ""
for line in f:
  stripped_line = line.rstrip()
  string_without_line_breaks += '"' + stripped_line + '"' + ', '
f.write(string_without_line_breaks)
f.close()