'''
Code to extract the user details and verify it
'''

'''Import necessary modules'''
import re 


def get_name(name="Name"):
    '''Get name'''
    if not name.isalpha():
        return "Invalid Name"
    return name


def get_email(email="abc@gmail.com"):
    '''Get Email Id'''
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):  
        return email  
    return "Invalid Email" 


def get_phone_number(phone_no="0"):
    '''Get Phone Number'''
    if len(phone_no) != 10:
        return "Invalid Phone Number"
    if not phone_no.isnumeric():
        return "Invalid Phone Number"
    return phone_no


def get_gender(gender='na'):
    '''Get Gender'''
    gender_list = ['m', 'f', 'male', 'female']
    if gender.lower() not in gender_list:
        return "Invalid Gender"
    return gender
