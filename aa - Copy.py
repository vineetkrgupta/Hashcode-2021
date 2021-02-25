
# try this code
fileno="e"
filename = "input/"+fileno+".txt"
f = open(filename, 'r')
x = f.readline()

s = x.split(" ")
loop = int(s[2])
lis = []
maintext = ""


def searc(a):
    f.seek(0, 0)
    f.readline()
    xa = []
    for i in range(loop):
        m = f.readline()
        m = m.split(" ")
        if(m[1] == a):
            xa.append(m[2])
    return len(xa), xa


def main():
    global maintext
    d = open(filename, 'r')
    d.readline()

    for i in range(loop):
        m = d.readline()
        ma = m.split(" ")
        try:
            x = ma[1]
        except:
            print(m)
        if x in lis:
            pass
        else:
            lis.append(x)
            # print(x)
            maintext = maintext + x + " \n"
            dh, h = searc(x)
            # print(dh)
            maintext = maintext + str(dh) + " \n"
            for element in h:
                #print(element," 1")
                maintext = maintext + element + " 1\n"


main()
maintext = str(len(lis))+"\n"+maintext
print(maintext)
filew= open(fileno+".txt", 'w+')
filew.write(maintext)
filew.close()