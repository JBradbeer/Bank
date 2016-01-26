from sys import argv


def new_user():
    name = raw_input("please enter your name")
    name = name.split(" ")

    script, atmdatabase = argv

    try:
        db = open(atmdatabase.txt)
        line = (db.readline()[-1]).split(" ")
        id = line[0]

        db.write(id + name[0:1])

        db.close()
    except ():
        print ("ISSUE finding the database")
