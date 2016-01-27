from sys import argv

script, atmdatabase = sys.argv  #this line crashes code

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

