FILEPATH = "test.txt"
def get_todo(filepath=FILEPATH):
    """ read a text file and return the list
       of to do """
    with open(filepath, "r") as my_file:
        to_do_local = my_file.readlines()

    return to_do_local


#print(help(get_todo("../test.txt")))


def write_todo(to_do_argument, filepath="test.txt"):
    """ write a text file and return the list
    of to do """
    with open(filepath, 'w') as file:
        file.writelines(to_do_argument)
if __name__== "__main__":
    print(get_todo())