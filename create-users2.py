#!/usr/bin/python3

# INET4031
# Devin Xiong
# 3/22/26
# 3/23/26

# os runs linux system commands from the python script
# re checks whether a line starts with # so it can be skipped
# sys reads the input line by line from the input file

import os
import re
import sys

def main():
    # ask user if they want to do a dry run
    with open("/dev/tty", "r") as keyboard:
        print("Would you like to do a dry run? Y for yes, N for no: ", end="", flush=True)
        dry_run_input = keyboard.readline().strip().upper()

    dry_run = dry_run_input == "Y"

    # reads each line from input (create-users.input)
    for line in sys.stdin:
        original_line = line.strip()

        # checks if the line starts with #, if it does it should be skipped
        match = re.match("^#", line)

        # removes extra whitespace and splits the line into fields using colons
        fields = line.strip().split(':')

        # skips the line if it's commented out or doesn't contain the required 5 fields
        # in dry run mode, print a message showing that the line was skipped
        if match:
            if dry_run:
                print("Skipping line because it's marked with a #: %s" % original_line)
            continue

        if len(fields) != 5:
            if dry_run:
                print("Error: line doesn't have enough fields and was skipped: %s" % original_line)
            continue

        # stores the username and password from input
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # split the group field by commas 
        groups = fields[4].split(',')

        # print a message showing that account is going to be made
        print("==> Creating account for %s..." % username)

        # builds the linux adduser command to create accounts without prompting for a password and sets the username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # during a dry run, print the command that would be executed
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # print a message showing that the password is about to be set
        print("==> Setting the password for %s..." % username)

        # builds the command that sends the password into passwd so the user's password can be set
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # print the command that would have run during dry-run
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # go through each group listed for the user
        for group in groups:

            # if line has a dash then user should not be added to any groups
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
