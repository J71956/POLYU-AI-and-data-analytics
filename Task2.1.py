First_name = str(input("What is your first name?"))
Last_name = str(input("What is your last name?"))
opt = int(input("Which name you want to be addressed as? press 1 for First name, 2 for Last Name"))
if opt == 1:
    print('Hello' + First_name + '! Your first name has' + str(len(First_name)) + 'leters and' + str(len(Last_name)) + 'characters in second name')
elif opt == 2:
    print('Hello ' + Last_name + '! Your first name has' + str(len(First_name)) + ' letters and ' + str(len(Last_name)) + ' characters in second name')    