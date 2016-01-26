from sys import argv

def rec_user():
    user_id = input("please enter your ID")

    script, atmdatabase = argv
    with open(atmdatabase.txt) as db:
        for line in db:  # this is inefficient as it will run n times
            if line.split(" ")[0] == user_id:
                true_info = line
                print true_info
