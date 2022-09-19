from re import search

usr_inp = input("Enter more than 4 characters: ")
passwd = usr_inp if len(usr_inp) >=4 else ""
rgx = ['\W', '[a-z]', '[A-Z]', '\d']
match = [x for x in rgx if search(x, passwd)]
if len(match) == 4:
    print(f'Yes, "{passwd}" string satisfied complexity policy.')
else:
    print(f'No, "{passwd}" string not satisfied complexity policy.')
