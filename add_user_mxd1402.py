#!/bin/bash

#Max Deng

import os 
import csv
import string

PASSWORD = "password"                                            

def read_csv(filename):                                      
    
    flist = []
    rlist = []

    with open(filename, 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        
        flist = next(csv_reader)

        for row in csv_reader:
            rlist.append(row)
    
    return rlist

def add_users(ulist):                                       

    added_users = list()
    count = 1

    for i in range(len(user_info)):

        if(i == len(user_info)):
            break
        
        else:

            id = str(ulist[i][0])
            last_name= str(ulist[i][1])
            first_name= str(ulist[i][2])
            first_letter = str(ulist[i][2][:1])
            office = str(ulist[i][3])
            phone = str(ulist[i][4])
            department = str(ulist[i][5])
            group = str(ulist[i][6])
           
        
            username = first_letter + last_name

            for i in range(len(username) -1):
                if username[i] == "'":
                   username = username.replace("'","")
                else:
                    continue
                
            lowername = username.lower()

            home_directory = "/home/" + department + "/" + lowername

            if(lowername in added_users):
                lowername += str(count)
                added_users.append(lowername)
            else:
                added_users.append(lowername)

            if group == "office":
                shell = "/bin/csh"
            else:
                shell = "/bin/bash"
            
            if(id != "" and first_name != "" and last_name != "" and office != "" and phone != "" and department != "" and group != ""):
                print("Processing employee ID " + id + ".\t" + lowername + " added to system\n")
                os.system("sudo useradd " + lowername +" -d " + home_directory +" -s "+ shell +" -g " + group + " -p " + PASSWORD )
                os.system("sudo chage -d 0 " + lowername)

            elif (id == "" or first_name == "" or last_name == "" or office == ""  or group == ""):
                print("Cannot process ID " + id + ".\tInsufficient data.\n")

            elif(group != "pubsafety" or group != "office" or group == ""):
                print("Cannot process ID " + id + ".\tNot a valid group\n")


if __name__ == '__main__':

    os.system("clear")
    os.system("sudo groupadd -f office")
    os.system("sudo groupadd -f pubsafety")
    os.chdir("/home")
    os.system("sudo mkdir ceo")
    os.system("sudo mkdir security")
    os.chdir("/home/student/Downloads")
    print("Adding new users to the system.")
    print("Please Note: The default password for new users is password")
    print("For testing purposes. Change the password 1$4pizz@.\n")

    user_info = read_csv("linux_users.csv")

    add_users(user_info)
