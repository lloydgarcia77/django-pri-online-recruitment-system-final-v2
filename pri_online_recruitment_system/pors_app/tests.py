from django.test import TestCase 
import functools
import operator 

from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings 

from datetime import datetime

import string
import random

#this is your "password/ENCRYPT_KEY". keep it in settings.py file
#key = Fernet.generate_key() 


def ecrypt_key(txt):
    try:
        # convert integer etc to string first   
        txt = str(txt)
        # get key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text =base64.urlsafe_b64encode(encrypted_text).decode("ascii")

        return encrypted_text

    except Exception as e:
        # log if an error
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


print(ecrypt_key(1))











# Create your tests here.
#https://www.geeksforgeeks.org/reduce-in-python/

lis = [1,2,3,4,5]
names = ["lloyd","Queen","Lord"]

output = functools.reduce(operator.add, lis)

print(output)

# output2 = functools.reduce(operator.and_, names)

# print(output2)

print(operator.add(6,7))
print(operator.and_(6,7))
 

#flip 1-0 = 0 / 1-1 = 1
#0110 0000 = 6
#1110 0000 = 7 
#0110 0000 = 6
 
print("-----------------------------")

 



# https://stackabuse.com/how-to-format-dates-in-python/

#Dec. 1, 2019, 5:24 p.m.
#YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."]

# my_date = datetime.datetime.strptime('Oct 15 2020 12:10 PM', '%b %d %Y %I:%M %p')
# print(my_date)
# new_date = my_date.strftime('%Y-%m-%d %H:%M:%S')

# print(new_date)
# final_date = my_date.strftime('%b %d %Y %I:%M %p')

# print(final_date)


# for i in range(1, 61, 1):
#     print(str('question'+str(i)+' = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="x")'))

# over = 50
# score = 50
# exam_score = score/over

# print(exam_score)

# if exam_score > 0 and exam_score < 0.25:
#     print('Poor')
# elif exam_score > 0.25 and exam_score < 0.50:
#     print('Below Average')

# elif exam_score > 0.50 and exam_score < 0.75:
#     print('Average')

# elif exam_score > 0.75 and exam_score <= 1.0:
#     print('Outstanding')


# https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
# https://pynative.com/python-generate-random-string/
def randomApplicantId(string_length=7):
    numbers = string.digits
    letters = string.ascii_uppercase

    id = ''.join(random.choice(letters + numbers) for i in range(string_length))

    return id

print("Auto Generated id: ",randomApplicantId(7))


