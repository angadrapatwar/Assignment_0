#registration and login system with python

while True:
    import string
    import json

    # if json file does not exist the try statement will generate a json file at the start itself
    try:
        with open("sample_file.json", "x") as file:
            file.write('{"user":"password"}')  # the format in which the json file will be used

    # if json file already exists the except statement will run through the program
    except:
        while True:
            a = input("You wish to login or register? \n")
            if a == 'register':  # if the user chooses to register
                b = input('e-mail ID (Username) : ')
                c = list(b)

                # task 1
                if '@' not in c or '.' not in c:
                    print('Invalid e-mail ID,provide a valid e-mail address')
                    break

                # task 2
                if abs(c.index(".") - c.index("@")) == 1:
                    print('Invalid e-mail ID, @ and . are not allowed together')
                    break

                # task 3
                if c[0].isnumeric() == True:
                    print('Invalid e-mail ID,numbers not allowed at the start')
                    break

                # task 4
                if c[0] in string.punctuation:
                    print('Invalid e-mail ID,special characters not allowed at the start')
                    break

                # after a valid email id password is to be generated
                else:
                    d = input('password : ')
                    e = list(d)
                    for i in range(len(e) + 1):

                        # password task 1
                        pun = (string.punctuation)
                        pun1 = any(x for x in pun if x in e)
                        if pun1 != True:
                            print("password must contain at least one special character")
                            break

                        # password task 2
                        no = any(e[i] for i in range(len(e)) if e[i].isnumeric() == True)
                        if no != True:
                            print('password must contain at least one number')
                            break

                        # password task 3
                        upp = any(e[i] for i in range(len(e)) if e[i].isupper() == True)
                        if upp != True:
                            print('password must contain at least one upper case character')
                            break

                        # password task 4
                        low = any(e[i] for i in range(len(e)) if e[i].islower() == True)
                        if low != True:
                            print('password must contain at least one lower case character')
                            break

                        # password task 5
                        elif len(e) < 5:
                            print("length of password too short")
                            break

                        # password task 6
                        elif len(e) > 16:
                            print("lenght of password too long")
                            break

                        # A json file is generated where all the details of the user are stored
                        with open("sample_file.json", "r+") as file:
                            data = json.load(file)
                            data.update(
                                {f"{b}": f"{d}"})  # email and its corresponding password is stored in this format
                            file.seek(0)
                            json.dump(data, file)
                break

            if a == 'login':  # if the user chooses to login
                b1 = input("Username : ")

                # the provided email id is verified in the system json file
                with open("sample_file.json", "r+") as file:
                    data = json.load(file)

                # if the email id is verified, password is to be verified
                for j in data.values():
                    if b1 in data:
                        p = input("Password : ")

                        # after a valid password system is looged in successfully
                        if data[b1] == p:
                            print('logged in successfully')
                            break
                        # in case of wrong password two option pop-up
                        else:
                            print("wrong password")

                            # the two options are as provided
                            b2 = input('press 1 to restart or 2 to retrive password : ')
                            if b2 == '2':
                                print('retrived password after otp verification : ', data[b1])
                            if b2 == '1':
                                continue
                    if b1 not in data:
                        print('e mail id does not exist')
                        break
                continue











