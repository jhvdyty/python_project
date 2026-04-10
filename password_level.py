import re

def level_one(password):
    flag, flag2 = False, False 
    for i in password:
        if i.isalpha():
            flag = True  
        elif i.isdigit():
            flag2 = True

    if len(password) > 3 and flag and flag2:
        return 1

    return 0

def level_two(password, last_level):
    easy_password = ["qwerty","11111","qqqqq","66666","zxcvbn", "1234"] 
    flag = True 
    for i in easy_password:
        if i in password:
            flag = False


    if len(password) > 6 and last_level and flag:
        return 1 
    
    return 0

def level_thri(password, last_level):

    flag = False 

    special_characters = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'

    for i in special_characters:
        if i in password:
            flag = True

    if len(password) > 8 and last_level and flag and password != password.lower():
        return 1 

    return 0


def main():
    print ("enter you password: ")
    password = str(input())

    if level_thri(password, level_two(password, level_one(password))):
        print ("youre password is very good - 3 level")
    elif level_two(password, level_one(password)):
       print ("youre password is 2 level")
    elif level_one(password):
        print ("youre password is only 1 level")
    else:
        print ("youre password is very bad")




main()