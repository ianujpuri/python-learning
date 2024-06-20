
def write_file(filename):
    myfile = open(filename, 'w+')

    for i in range(1,10,1):
        myfile.write("Text at line " + str(i) +"\n")

    myfile.close()


def read_file(filename):
    myfile = open(filename, 'r')
    if(myfile.mode == 'r'):
        lines = myfile.readlines()
        print(lines)

def append_file(filename):
    myfile = open(filename, 'a+')
    if(myfile.mode == 'a+'):
        for i in range(1, 5, 1):
            myfile.write("more text \n")


write_file("sample.txt")

read_file("sample.txt")

append_file("sample.txt")

read_file("sample.txt")


