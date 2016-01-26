from sys import argv

script, atmdatabase = sys.argv

def new_user():
    name = raw_input("please enter your name")
    name = name.split(" ")

    try:
        db = open(atmdatabase.txt)
        line = (db.readline()[-1]).split(" ")
        id = line[0]

        db.write(id + name[0:1])

        db.close()
    except ():
        print ("ISSUE finding the database")


def rec_user():
    user_id = input("please enter your ID")

    with open(atmdatabase.txt) as db:
        for line in db:  # this is inefficient as it will run n times
            if line.split(" ")[0] == user_id:
                true_info = line
                print true_info
