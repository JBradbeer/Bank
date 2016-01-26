import sys

from user_create import new_user


def rec_user():
    user_id = input("please enter your ID")

    script, atmdatabase = sys.argv

    with open(atmdatabase.txt) as db:
        for line in db:  # this is inefficient as it will run n times
            if line.split(" ")[0] == user_id:
                true_info = line
                print true_info


responded = False
while not responded:
    new_rec = raw_input("Are you a new user?")

    if new_rec == 'yes':
        new_user()
        responded = True
    elif new_rec == 'no':
        rec_user()
        responded = True
    else:
        print "please enter yes/no"
