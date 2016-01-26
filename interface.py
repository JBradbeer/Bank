from user_create import *
from sys import *

def rec_user():
    user_id = input("please enter your ID")

    script, atmdatabase = argv

    with open(atmdatabase.txt) as db:
        x = True
        for line in db:  #this is inefficiant as it will run n times no matter what
            if line.split(" ")[0] == user_id:
                true_info = line


x = True
while x:
    new_rec = raw_input("Are you a new user?")

    if new_rec == 'yes':
        new_user()
        x = False
    elif new_rec == 'no':
        rec_user()
        x = False
    else:
        print "please enter yes/no"






