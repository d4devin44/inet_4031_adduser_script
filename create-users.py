#!/usr/bin/python3

# INET4031
# Devin
# 3/21/26
# 3/22/26

#os runs linux system commands from the python script
#re checks whether a line starts with # so it can be skipped
#sys reads input line by line from the input file

import os
import re
import sys

def main():
    #reads each line from input (create-users.input)
    for line in sys.stdin:

        #checks if the line start with #, means it's commented out and should be skipped
        match = re.match("^#",line)



	#removes whitespace and split the line into fields using colons
        fields = line.strip().split(':')

        #skips the line if it's commented out or doesn't contain the 5 fields
        if match or len(fields) != 5:
            continue

        #stores the username and password 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #split the group field by commas so it can process multiple groups for one user by the script
        groups = fields[4].split(',')

        #print message showing that a new user is being createdt
        print("==> Creating account for %s..." % (username))

        #builds the linux adduser command to create accounts without prompting for a password and sets the username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #prints cmd that is going to be printed 
        print(cmd)
        os.system(cmd)

        #print a message showing that the password is about to be set
        print("==> Setting the password for %s..." % (username))

        # sends the password into passwd to set password 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #prints cmd that is going to be printed
        print(cmd)
        os.system(cmd)

        for group in groups:

            # if the value is not a dash, add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

