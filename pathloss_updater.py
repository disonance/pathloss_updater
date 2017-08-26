filename = raw_input("input file -> ")


f1 = open(filename,"r+")
f2 = open("new.txt","w+")

for row in f1:
    eol=len(row)
    line = "\"at@nvm"+ row[0:eol-1] + "}\",\n"
    print "\"at@"+ row[0:eol-1] + "}\",\n"
    f2.write(line)


