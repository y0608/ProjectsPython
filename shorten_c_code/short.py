import sys


def remove_comments(source):
    print(source)
    
def main(original_file):
    with open(original_file, "r") as input:
        with open('nc'+original_file, "w") as output:
            for line in input:
                print(line)
    input.close()
    output.close()

    # file = open(file_name,'r')
    # new_file = open(str('nc'+file_name),'w')
    # source = file.read()
    # remove_comments(source)
    # new_file.write(source)
    # file.close()
    # new_file.close()


main(str(sys.argv[1]))