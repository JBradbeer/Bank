import sys

from user_create import new_user
from bank_func import user_login
 
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
