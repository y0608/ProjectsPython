import sys


def remove_comments(source):
    print(source)
    
def main(file_name):

    file = open(file_name,'r')
    new_file = open(str('nc'+file_name),'w')

    source = file.read()
    remove_comments(source)
    new_file.write(source)


    file.close()
    new_file.close()


main(str(sys.argv[1]))