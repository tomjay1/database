#create record
#update record
#read record
#delete record

#CRUD
import os

user_db_path = 'data/userrecord'

def create(accountnumber, userdetails):
    #print('create a new user record')
    completion_state = False
    try:
        f = open (user_db_path + str(accountnumber) + '.txt', 'x')
        
    except FileExistsError:

        print('user alrady exist')
        #delete the already created file, and print out error, then return false
        return completion_state
    else:
        f.write(str(userdetails));

    finally:
        f.close();

    return completion_state

    #CREATE A FILE
    #NAME OF FILE = accountnumber.txt 
    #add the user details to the file
    #return true

def read(useraccountnumber):
    print('read user record')
    #find users with account number
    #fetch content of the file
    #if saving to file fails then delete file

def update(useraccountnumber):
    print('update user record')
    #find user with account number
    #fetch the content of the fie
    #update the content of the file
    #save the file


def delete(useraccountnumber):
    print('delete user record')

    if os.path.exist(user_db_path +str(useraccountnumber)+ '.txt'):
        os.remove(user_db_path + str(useraccountnumber)+'.txt')

    #find user with account number
    #delete user reord(file)
    #return true


def find(useraccountnumber):
    print('find user')
    #find user record in the data folder

    #create(9916842872, ['tomjay','jay jay','tom@gmail.com', 'tmoney', 50000]);