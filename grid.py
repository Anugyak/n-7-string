#function to print the character C in n*7 grid using loop
def printc():
    #loop for the row in the grid
    for row in range(7):
        #loop for column in the grid
        for col in range(6):
            #if statement to print the * for the character C
            if(col == 1 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and ( col > 1 and col < 5)) or (col == 5 and (row == 1 or row == 5)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

#function to print the character C in n*7 grid using loop
def prints():
    #loop for row in the grid
    for row in range(7):
        #loop for column in the grid
        for col in range(6):
            #if statement to print the character s with *
            if ((row == 0 or row == 3 or row == 6) and (col > 1 and col < 5)) or (col == 0 and (row != 0 and row != 4 and row != 6)) or (col == 5 and (row != 0 and row != 2 and row != 6)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

#function to print the character 1 in n*7 grid using loop
def print1():
    #loop for row in the n*7 grid
    for row in range(7):
        #loop for column in the n*7 grid
        for col in range(6):
            #if statement to print * for the character 1
            if(row == 6 and col != 0) or (col == 3) or (row == 2 and ( col > 0 and col < 2)) or (row == 1 and (col <3 and col > 1)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

#function to print the character 4 in n*7 grid using loop
def print4():
    #for loop for row in n*7 grid
    for row in range(7):
        #for loop for column in n*7 grid
        for col in range(6):
            #if statement to print * for 4
            if(col == 4) or (row ==4 and col != 0) or (row == 2 and ( col > 1 and col < 3)) or (row == 1 and (col < 4 and col > 2)) or (row == 3 and (col < 2 and col > 0)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

#function to print the character 0 in n*7 grid using loop
def print0():
    #loop for row in the grid
    for row in range(7):
        #loop for column in the grid
        for col in range(6):
            #if statement to print * for 0
            if((col == 1 or col == 5) and (row != 0 and row != 1 and row != 5 and row != 6)) or ((row == 0 or row == 6) and (col > 2 and col < 4)) or ((row == 1 or row == 5) and (col > 1 and col <5 and col != 3)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

#function to print the character CSC in n*7 grid using loop
def printcsc():
    #loop for row in n*7 grid
    for row in range(7):
        #loop for column in n*7 grid
        for col in range(18):
            #if condition to print * for CSC
            if(col == 1 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and ( col > 1 and col < 5)) or (col == 5 and (row == 1 or row == 5)) or ((row == 0 or row == 3 or row == 6) and (col > 7 and col < 11)) or (col == 7 and (row != 0 and row != 4 and row != 6)) or (col == 11 and (row != 0 and row != 2 and row != 6)) or (col == 13 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and ( col > 13 and col < 17)) or (col == 17 and (row == 1 or row == 5)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

#function to print the character 1401 in n*7 grid using loop
def print1401():
    ##loop for row in n*7 grid
    for row in range(7):
        #loop for column in n*7 grid
        for col in range(24):
            if(row == 6 and col != 13 and col!=16 and col!=17 and col!=18 and col!=14 and col != 0 and col!=6 and col != 12 and col !=7 and col!=8 and col!=9 and col!=11) or (col == 3) or (row == 2 and ( col > 0 and col < 2)) or (row == 1 and (col <3 and col > 1)) or (col == 10) or (row ==4 and col!=19 and col!=20 and col!=22 and col!=23 and col != 6 and col != 12 and col != 2 and col != 1 and col != 0 and col != 4 and col != 5 and col!=15 and col!=14 and col != 16 and col!=18) or (row == 2 and ( col > 7 and col < 9)) or (row == 1 and (col < 10 and col > 8)) or (row == 3 and (col < 8 and col > 6)) or ((col == 13 or col == 17) and (row != 0 and row != 1 and row != 5 and row != 6)) or ((row == 0 or row == 6) and (col > 14 and col < 16)) or ((row == 1 or row == 5) and (col > 13 and col <17 and col != 15)) or (row == 6 and col!=0 and col!=6 and col!=12 and col!=7 and col!=8 and col!=9 and col!=11 and col!=13 and col!=14 and col!=16 and col!=17 and col != 18) or (col == 21) or (row == 2 and ( col > 18 and col < 20)) or (row == 1 and (col <21 and col > 19)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

def print_string(s):
    # Loop through the characters in the string and print each one
    if s.upper() == 'C':
        printc()
    elif s.upper() == 'S':
        prints()
    elif s.upper() == '1':
        print1()
    elif s.upper() == '4':
        print4()
    elif s.upper() == '0':
        print0()
    elif s.upper() == 'CSC':
        printcsc()
    elif s.upper() == '1401':
        print1401()

def main():
    while True:
        # Get a string from the user
        s = input("Enter a string (or 'BREAK' to stop): ")

        # Check if the user wants to stop and enter BREAK to stop
        if s == 'BREAK':
            break
        #else if the user input the mentioned characters print the string in n*7 grid
        elif s.upper() in ['C', 'S', '1', '4', '0', 'CSC', "1401"]:
        # Do something with the valid character
            print("Valid character entered:", s)
            print_string(s)
        else:
            # Alert the user that the input is invalid and ask them to re-enter
            print("Error: invalid input. Please enter a string containing only the characters 'C', 'S', '1', '4', and '0'.")
            continue

if __name__ == '__main__':
    main()